{% for message in previous_messages %}
{% if message['is_my_message'] %}
Me: {{ message['text'] }}
{% else %}
Them: {{ message['text'] }}
{% endif %}
{% endfor %}
