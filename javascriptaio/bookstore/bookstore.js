const bookstore = {
  books: ["Ulysses", "The Great Gatsby"],
  removeBook(title) {
    let newList = this.books.filter((book) => book != title);
    this.books = newList;
    this.displayBookstore();
  },
  displayBookstore() {
    const renderTarget = document.getElementById("bookstore");
    const booklist = this.books.map((book) => `<p>${book}</p>`);
    renderTarget.innerHTML = booklist.join("");

    shoppingCart.displayCart(this.removeBook.bind(this));
  },
};

const shoppingCart = {
  itemsInCart: ["The Great Gatsby"],
  handleClick(removeBook) {
    removeBook(this.itemsInCart);
  },
  displayCart(clickHandler) {
    const renderTarget = document.getElementById("cart");
    const itemsInCart = this.itemsInCart.map((item) => `<p>${item}</p>`);
    const checkOutButton = `<button id='checkout'>Check out</button>`;
    renderTarget.innerHTML = itemsInCart.join("") + checkOutButton;
    document.getElementById("checkout");
    document.addEventListener("click", () => this.handleClick(clickHandler));
  },
};
bookstore.displayBookstore();
