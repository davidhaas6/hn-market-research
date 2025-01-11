import pandas as pd

def create_html_from_comments(df, output_filepath=None, title="HackerNews Comments"):
    """
    Generates an HTML file displaying comments and their associated tags,
    including a link to the HN comment, and the ability to filter by tag using AND/OR logic.

    Args:
        df (pd.DataFrame): A pandas DataFrame with columns 'id', 'text', and 'labels'.
        output_filepath (str, optional): The path where the HTML file will be saved.
        title (str, optional): The title that will appear in the browser tab.
    """
    if output_filepath is None:
        timestamp = pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')
        output_filepath = f"out/comments_{timestamp}.html"
    
    all_tags = set()
    for _, row in df.iterrows():
        if row['labels']:
           all_tags.update(row['labels'])
    all_tags = sorted(list(all_tags))
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <style>
            body {{
                font-family: sans-serif;
                margin: 20px;
            }}
             #content-container {{
                display: flex;
                max-width: 1200px; /* Sets a max width for the content */
                margin: 0 auto;  /* Center the container */
            }}
            #filter-container {{
                width: fit-content;
                padding-right: 20px;
                border-right: 1px solid #ddd;
           }}
            #filter-container h2 {{ margin-top: 0; }}
            #filter-container div {{ margin-bottom: 5px; }}
            #comment-list {{ 
                flex: 1;
                overflow-y: auto;
            }}
            .comment-container {{ border: 1px solid #ddd; padding: 15px; margin-bottom: 15px; }}
            .comment-header {{ display: flex; align-items: center; margin-bottom: 5px; }}
            .comment-header a {{ text-decoration: none; margin-left: 8px; }}
            .comment-text {{ margin-bottom: 10px; }}
            .tag {{ display: inline-block; background-color: #f0f0f0; padding: 3px 8px; margin-right: 5px; border-radius: 3px; font-size: 0.85em; }}
           .filter-checkbox-container {{ display: flex; align-items: center; margin-bottom: 3px; }}
             .filter-checkbox {{ margin-right: 5px; }}
           
            .hidden {{ display: none; }}
        </style>
    </head>
    <body>
        <div id="content-container">
            <div id="filter-container">
                <h2>Filter by Tag</h2>
                <div>
                    <input type="radio" id="filter-or" name="filter-type" value="or" checked onchange="filterComments()">
                    <label for="filter-or">OR</label><br>
                    <input type="radio" id="filter-and" name="filter-type" value="and" onchange="filterComments()">
                    <label for="filter-and">AND</label>
                </div>
                """
    for tag in all_tags:
      html_content += f"""
            <div class="filter-checkbox-container">
               <input type="checkbox" id="{tag}" value="{tag}" class="filter-checkbox" onchange="filterComments()">
               <label for="{tag}">{tag}</label>
           </div>
        """
    html_content += f"""
            </div>
            <div id="comment-list">
                <h1>{title}</h1>
        """

    for index, row in df.iterrows():
        comment = row['text']
        tags = row['labels']
        comment_id = row['id']
        hn_link = f"https://news.ycombinator.com/item?id={comment_id}"

        tags_str = " ".join(tags) if tags else "" # added tags_str to be searchable by javascript

        html_content += f"""
            <div class="comment-container" data-tags="{tags_str}">
                <div class="comment-header">
                    Comment ID: {comment_id}
                    <a href="{hn_link}" target="_blank">View on HN</a>
                </div>
                <p class="comment-text">{comment}</p>
                <div>
                    {" ".join([f'<span class="tag">{tag}</span>' for tag in tags]) if tags else ""}
                </div>
            </div>
        """
    html_content += """
        </div>
        </div>
        <script>
            function filterComments() {
                const selectedTags = Array.from(document.querySelectorAll('input[type="checkbox"]:checked'))
                    .map(checkbox => checkbox.value);
                const commentContainers = document.querySelectorAll('.comment-container');
                const filterType = document.querySelector('input[name="filter-type"]:checked').value;


                commentContainers.forEach(container => {
                    const commentTags = container.getAttribute('data-tags').split(" ");
                    let shouldShow = false;
                     if (selectedTags.length === 0) {
                        shouldShow = true
                    } else if(filterType === 'or'){
                        shouldShow = selectedTags.some(tag => commentTags.includes(tag));
                    } else if(filterType === 'and'){
                       shouldShow = selectedTags.every(tag => commentTags.includes(tag));
                    }

                    if (shouldShow) {
                      container.classList.remove('hidden');
                    } else {
                         container.classList.add('hidden');
                    }
                });
             }
        </script>
    </body>
    </html>
    """

    with open(output_filepath, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"HTML file saved to: {output_filepath}")


if __name__ == '__main__':
    # Example usage:
    data = {
        'id': [40814477, 40815826, 40816458, 40816541, 40818011, 40818012, 40818013, 40818014],
        'text': [
            "This is a fascinating discussion!",
            "I completely disagree with that point.",
            "One I thought was kind of silly that I made wa...",
            "you ask what i mean about programmer productiv...",
             "I use it for similar reasons! But I do not hav...",
             "I really enjoyed this comment!",
             "I like to debate the merits of a programming language",
             "I find this analysis to be too difficult to follow!",
            "This is a really long comment that is designed to test how well the webpage handles a very long comment. Let's see how it displays!",
            "another very long comment, it should also test to make sure the container does not overflow. Another very long comment, it should also test to make sure the container does not overflow.Another very long comment, it should also test to make sure the container does not overflow.Another very long comment, it should also test to make sure the container does not overflow."
        ],
        'labels': [
            ["discussion", "interesting"],
            ["disagreement", "opinion"],
            ["silly"],
            ["programmer", "productivity"],
            ["reasons", "similar"],
            ["interesting", "enjoyed"],
             ["programming", "debate"],
              ["analysis", "difficult"]
             , ["test", "long"],
            ["test", "long", "overflow"]
        ]
    }
    df = pd.DataFrame(data)
    create_html_from_comments(df, title="Hacker News Thread Discussion")