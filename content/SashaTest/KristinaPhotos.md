Title: Kristinta photos
Date: 2017-07-13 23:51:25
Modified: 2018-02-05 17:53:44
Author: Sasha Chernykh
Lang: en
Summary: Photos of Kristina Kiva
Tags: Kristina
Category: Kristina
Pagecolors: sublime-text
Iconleftorright: right
gallery: {photo}Kristina
Jquery: true
Gemini: true
Jquerylazy: true
Fancybox: true

Beginning text

{% if photo_gallery %}
<div class="gallery">
        {% for title, gallery in photo_gallery %}
            <h1>{{ title }}</h1>
                {% for name, photo, thumb, exif, caption in gallery %}
                        <a href="{{ SITEURL }}/{{ photo }}" title="{{ name }}" exif="{{ exif }}" caption="{{ caption }}"><img src="{{ SITEURL }}/{{ thumb }}"></a>
                {% endfor %}
        {% endfor %}
</div>
{% endif %}

Ending text