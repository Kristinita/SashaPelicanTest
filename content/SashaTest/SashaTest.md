Title: ValeriyaSpeller
Date: 2017-07-13 23:51:25
Modified: 2018-02-05 12:07:40
Author: Sasha Chernykh
Lang: en
Summary: Search typos in Russian texts
Tags: sublime-text, yaspeller
Category: Sublime Text
Pagecolors: sublime-text
Iconleftorright: right
gallery: {photo}kris
photo_gallery: true
Jquery: true
Gemini: true
Jquerylazy: true
Fancybox: true

{% if article.photo_gallery %}
<div class="gallery">
        {% for title, gallery in article.photo_gallery %}
            <h1>{{ title }}</h1>
                {% for name, photo, thumb, exif, caption in gallery %}
                        <a href="{{ SITEURL }}/{{ photo }}" title="{{ name }}" exif="{{ exif }}" caption="{{ caption }}"><img src="{{ SITEURL }}/{{ thumb }}"></a>
                {% endfor %}
        {% endfor %}
</div>
{% endif %}