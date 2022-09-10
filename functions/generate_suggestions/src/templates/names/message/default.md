{% for message in previous_messages %}
{% if message['isMyMessage'] %}
{{ my_name }}: {{ message['text'] }}
{% else %}
{{ their_name }}: {{ message['text'] }}
{% endif %}
{% endfor %}
