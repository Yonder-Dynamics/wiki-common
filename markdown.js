var client = new XMLHttpRequest();
client.open('GET', 'wiki.md');
client.onreadystatechange = function() {
    var text      = client.responseText;
    var converter = new showdown.Converter();
    var options = [
        ['openLinksInNewWindow', true],
        ['metadata', true],
        ['simplifiedAutoLink', true],
        ['excludeTrailingPunctuationFromURLs', true],
        ['literalMidWordUnderscores', true],
        ['literalMidWordAsterisks', true],
        ['strikethrough', true],
        ['tables', true],
        ['tasklists', true],
        ['parseImgDimensions', true],
    ];
    options.forEach((pair)=>converter.setOption(pair[0] ,pair[1]));
    var html      = converter.makeHtml(text);
    var title     = converter.getMetadata().title
    if(title != undefined){
        document.title = title
    }
    document.getElementById("root").innerHTML = html;
}
client.send();