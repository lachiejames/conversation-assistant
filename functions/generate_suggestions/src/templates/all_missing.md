This is a casual conversation that I had with my friend:

{% for message in previous_messages %}
{{ message['author'] }}: {{ message['text'] }}
{% endfor %}

{{ my_name }}: