window.onscroll = function () {
  const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
  const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  const scrolled = (winScroll / height) * 100;
  document.getElementById("progress-bar").style.width = scrolled + "%";
};

// Sample HTML element for reference:
// <div id="progress-bar" style="height:5px;background:#29e;width:0;position:fixed;top:0;left:0;"></div>
