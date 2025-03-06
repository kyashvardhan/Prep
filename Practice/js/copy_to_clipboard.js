function copyToClipboard(text) {
  navigator.clipboard.writeText(text).then(() => {
    console.log("Text copied!");
  });
}

copyToClipboard("Hello, GitHub!");
