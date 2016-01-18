/**
 * Created by Wood on 2016/1/18.
 */
//********* perf test
//Rows: 1044 cols:20. total cells : 20880
//Chrom:    Old 1.327s  New: 0.037s 35.86 times
//IE:       Old 10.937s New: 0.185s 59.12 times
//Old is Jquery Json to table script
//New: Current script

function createTable(jsonTblObj, containerID, className, createHeader)
{
    if(jsonTblObj.length == 0 || containerID.length == 0)
        return;
    var tblContainer = document.getElementById(containerID);
    tblContainer.innerHTML = createTableHtml(jsonTblObj, className, createHeader);
}


function createTableHtml(jsonTblObj, className, createHeader)
{
    var html = "<table ";
    //add class
    if(className.length > 0)
    {
        html += "class='" + className + "'";
    }
    html += ">";
    //create header
    if(createHeader)
    {
        html+=createTheadHtml(jsonTblObj[0]);
    }
    //create body
    for(var row in jsonTblObj)
    {
        html += createTrHtml(jsonTblObj[row]);
    }
    return html + "</table>";
}


function createTrHtml(jsonRowObj)
{
    var html = '<tr>';
    for( var col in jsonRowObj)
    {
        var data = jsonRowObj[col];
        if(typeof data === 'string')
        {
            data = htmlEncode(data);
        }
        html += '<td>' + data + '</td>';
    }
    return html + "</tr>";
}


function createTheadHtml(jsonRowObj)
{
    var html = '<thead><tr>';
    for(var col in jsonRowObj)
    {
        var data = col;
        if(typeof data === 'string')
        {
            data = htmlEncode(data);
        }
        html += '<td>' + data + '</td>';
    }
    return html + "</tr></thead>";
}

//most effective html encode
//see https://jsperf.com/htmlencoderegex/75
function htmlEncode(html)
{
    return html.replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/'/g, '&#39;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}
