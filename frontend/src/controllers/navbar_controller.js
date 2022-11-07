import { Controller } from "@hotwired/stimulus";
import Cookies from "js-cookie";

export default class extends Controller {

  static values = {
    theme: String,
  };

  connect() {
    this.themeValue = this.getTheme();
    if (
      this.themeValue === "dark" &&
      !document.querySelector("html").classList.contains("dark")
    ) {
      this.toggleTheme();
    }
  }

  getTheme() {
    let theme;
    let cookieTheme = Cookies.get("theme");
    if (
      cookieTheme === "dark" ||
      (!cookieTheme &&
        window.matchMedia("(prefers-color-scheme: dark)").matches)
    ) {
      theme = "dark";
    } else {
      theme = "light";
    }

    return theme;
  }

  setTheme(value) {
    // write theme to cookie
    this.themeValue = value;
    Cookies.set("theme", value);
  }

  toggleTheme() {
    const buttonElement = this.element.querySelector('#dark-mode-toggler');
    document.querySelector("html").classList.toggle("dark");

    const svgArray = buttonElement.querySelectorAll("svg");

    svgArray.forEach(function (svgElement) {
      svgElement.classList.toggle("block");
      svgElement.classList.toggle("hidden");
    });
  }

  toggleDarkMode() {
    this.toggleTheme();

    if (this.themeValue === "light") {
      this.setTheme("dark");
    } else {
      this.setTheme("light");
    }
  }

  toggleMobileMenu() {
    const buttonElement = this.element.querySelector("#mobile-menu-button");
    const mobileMenu = this.element.querySelector("#mobile-menu");

    const svgArray = buttonElement.querySelectorAll("svg");

    svgArray.forEach(function (svgElement) {
      svgElement.classList.toggle("block");
      svgElement.classList.toggle("hidden");
    });

    mobileMenu.classList.toggle("hidden");
  }

}
