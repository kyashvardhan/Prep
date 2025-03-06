window.onscroll = () => {
  if (
    window.innerHeight + window.scrollY >=
    document.body.offsetHeight
  ) {
    console.log("Load more content...");
  }
};
