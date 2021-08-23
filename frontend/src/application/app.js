import "../styles/index.scss";

import "bootstrap/dist/js/bootstrap.bundle";
import { setupComment } from "../components/comment";

window.AccordBox = {
  setupComment: setupComment
};

window.document.addEventListener("DOMContentLoaded", function () {
  window.console.log("dom ready 1");
});
