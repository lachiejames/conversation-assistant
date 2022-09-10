{% for message in previous_messages %}
{{ message['author'] }}: {{ message['text'] }}
{% endfor %}
