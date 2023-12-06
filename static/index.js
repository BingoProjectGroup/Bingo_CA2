function showContent(page) {
    // Hide all content divs
    var contentDivs = document.getElementsByClassName("content");
    for (var i = 0; i < contentDivs.length; i++) {
      contentDivs[i].style.display = "none";
    }
  
    // Show the selected content
    var selectedContent = document.getElementById(page);
    if (selectedContent) {
      selectedContent.style.display = "block";
    }
  }
  