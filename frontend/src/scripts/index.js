import "../styles/index.scss";

import $ from "jquery/dist/jquery.slim";
import "bootstrap/dist/js/bootstrap.bundle";
import { setupComment } from "./components/comment";

window.AccordBox = {
  setupComment: setupComment
};

$(function () {
  window.console.log("dom ready");
});
