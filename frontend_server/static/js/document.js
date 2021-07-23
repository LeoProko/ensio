textarea = document.getElementsByTagName("textarea");
for (let i = 0; i < textarea.length; ++i) {
    textarea[i].setAttribute("style", "height:" + (textarea[i].scrollHeight) + "px;");
    textarea[i].addEventListener("input", auto_resize, false);
}

function auto_resize() {
    //this.style.height = '0px';
    this.style.height = this.scrollHeight - 20 + 'px';
}
