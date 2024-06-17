import os

# 定义项目结构
project_structure = {
    'templates': [
        'index.html', 'products.html', 'ai.html', 'game.html', 'blog.html', 'apps.html',
        'app_a.html', 'app_b.html', 'support.html', 'contact.html', 'about.html'
    ]
}

# 基本HTML模板
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="{{{{ url_for('static', filename='css/styles.css') }}}}">
</head>
<body>
    <nav>
        <div class="logo"><a href="{{{{ url_for('home') }}}}">Athmyx</a></div>
        <ul>
            <li><a href="{{{{ url_for('home') }}}}">Home</a></li>
            <li class="dropdown">
                <a href="{{{{ url_for('products') }}}}">Products</a>
                <div class="dropdown-content">
                    <a href="{{{{ url_for('ai') }}}}">AI</a>
                    <a href="{{{{ url_for('game') }}}}">Game</a>
                </div>
            </li>
            <li><a href="{{{{ url_for('blog') }}}}">Blog</a></li>
            <li class="dropdown">
                <a href="{{{{ url_for('apps') }}}}">Apps</a>
                <div class="dropdown-content">
                    <a href="{{{{ url_for('app_a') }}}}">A</a>
                    <a href="{{{{ url_for('app_b') }}}}">B</a>
                </div>
            </li>
            <li class="dropdown">
                <a href="{{{{ url_for('support') }}}}">Support</a>
                <div class="dropdown-content">
                    <a href="{{{{ url_for('contact') }}}}">Contact Us</a>
                    <a href="{{{{ url_for('about') }}}}">About</a>
                </div>
            </li>
        </ul>
    </nav>
    <main>
        <h1>{header}</h1>
        <p>{content}</p>
    </main>
    <footer>
        <p>&copy; 2024 Athmyx.</p>
    </footer>
</body>
</html>"""

# 页面内容定义
pages_content = {
#    'index.html': {'title': 'Athmyx Home', 'header': 'Welcome to Athmyx', 'content': 'Innovation and excellence at your fingertips.'},
    'products.html': {'title': 'Products - Athmyx', 'header': 'Products', 'content': 'Explore our range of products.'},
    'ai.html': {'title': 'AI Products - Athmyx', 'header': 'AI Products', 'content': 'Explore our AI products.'},
    'game.html': {'title': 'Game Products - Athmyx', 'header': 'Game Products', 'content': 'Explore our game products.'},
    'blog.html': {'title': 'Blog - Athmyx', 'header': 'Blog', 'content': 'Read our latest articles.'},
    'apps.html': {'title': 'Apps - Athmyx', 'header': 'Apps', 'content': 'Explore our apps.'},
    'app_a.html': {'title': 'App A - Athmyx', 'header': 'App A', 'content': 'Explore App A.'},
    'app_b.html': {'title': 'App B - Athmyx', 'header': 'App B', 'content': 'Explore App B.'},
    'support.html': {'title': 'Support - Athmyx', 'header': 'Support', 'content': 'How can we help you?'},
    'contact.html': {'title': 'Contact Us - Athmyx', 'header': 'Contact Us', 'content': 'Get in touch with us.'},
    'about.html': {'title': 'About - Athmyx', 'header': 'About Us', 'content': 'Learn more about us.'}
}

# 创建模板文件夹
if not os.path.exists('templates'):
    os.makedirs('templates')

# 生成HTML页面
for page, content in pages_content.items():
    with open(os.path.join('templates', page), 'w') as f:
        f.write(html_template.format(title=content['title'], header=content['header'], content=content['content']))

print("HTML pages generated successfully.")
