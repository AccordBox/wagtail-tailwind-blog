// This is the scss entry file
import "../styles/index.scss";

import { Application } from "@hotwired/stimulus";
import { definitionsFromContext } from "@hotwired/stimulus-webpack-helpers";
import Carousel from 'stimulus-carousel';
// load swiper css
import "swiper/css/bundle";

window.Stimulus = Application.start();
const context = require.context("../controllers", true, /\.js$/);
window.Stimulus.load(definitionsFromContext(context));

window.Stimulus.register('carousel', Carousel);
