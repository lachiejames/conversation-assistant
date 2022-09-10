{% for message in previous_messages %}
{% if message['isMyMessage'] %}
Me: {{ message['text'] }}
{% else %}
Them: {{ message['text'] }}
{% endif %}
{% endfor %}
