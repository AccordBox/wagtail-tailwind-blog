import axios from "axios";
import Tribute from "tributejs";
import camelcaseKeys from "camelcase-keys";
import snakecaseKeys from "snakecase-keys";

import { Controller } from "@hotwired/stimulus";

export default class extends Controller {
  connect() {
    const commentForm = this.element;
    const editorTextArea = commentForm.querySelector("#id_comment");

    getMentionTribute(commentForm).then(function (tribute) {
      if (tribute) {
        tribute.attach(editorTextArea);
      }
    });

    getEmojiTribute().then(function (tribute) {
      if (tribute) {
        tribute.attach(editorTextArea);
      }
    });
  }
}

async function getMentionTribute(commentForm) {
  const url = commentForm.dataset.mentionUrl;
  let tribute;

  try {
    const params = {
      objectPk: commentForm.dataset.objectPk,
      contentType: commentForm.dataset.contentType,
    };

    const response = await axios.get(url, {
      params: snakecaseKeys(params, { deep: true }),
    });
    const data = camelcaseKeys(response.data, { deep: true });

    let values = [];
    for (const index in data.result) {
      const userValue = data.result[index];
      values.push({
        key: userValue.userName,
        value: userValue.userName,
      });
    }

    tribute = new Tribute({
      values: values,
    });
  } catch (error) {
    console.error(error);
  }

  return tribute;
}

async function getEmojiTribute() {
  const url = 'https://api.github.com/emojis';
  let tribute;

  try {
    const response = await axios.get(url);
    const data = camelcaseKeys(response.data, {deep: true});

    let values = [];
    for (const key in data) {
      const value = data[key];
      values.push({
        key: key,
        value: value,
      });
    }
    tribute = new Tribute({
      trigger: ':',
      values: values,
      menuItemTemplate: function (item) {
        return `<img src="${item.original.value}"/>&nbsp;<small>:${item.original.key}:</small>`;
      },
      selectTemplate: function (item) {
        return `:${item.original.key}:`;
      },
      menuItemLimit: 5,
    });
  } catch (error) {
    console.error(error);
  }

  return tribute;
}
