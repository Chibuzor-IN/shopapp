function find(query, url, table) {
    if (query.length == 0) {
        return;
    }
    else {
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange = function() {
            if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                document.getElementById(table).innerHTML = xmlhttp.responseText;
            }
        }
        xmlhttp.open("GET", url + "?q=" + query, true);
        xmlhttp.send();
    }
}
function submit_form(form_id) {
	document.getElementById(form_id).submit();
}
function load(div_id) {
    words = ["show_items", "add_item", "edit_items"];
    i = words.indexOf(div_id);
    document.getElementById(words[(i+1)%3]).style.display = "none";
    document.getElementById(words[(i+2)%3]).style.display = "none";
    document.getElementById(words[i]).style.display = "block";
}
function delete_all() {
	items = document.getElementsByName('delete[]');
	for (var i=0; i<items.length; i++) {
		items[i].checked = true;
	}
	submit_form('del_item_form');
}