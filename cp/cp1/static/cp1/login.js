function validate(param)
{
	var username = document.getElementById("username").value;
	var password = document.getElementById("password").value;
	//{% for account in accounts %}
	if (username == param)
	{
		console.log("Login successfully");
	}
	else
	{
		console.log("param");
	}
	//{% endfor %}
}