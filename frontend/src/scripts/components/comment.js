import $ from "jquery/dist/jquery.slim";
import axios from "axios";
import Tribute from "tributejs";

async function getMentionTribute($commentsForm) {
  const url = $commentsForm.data("mention-url");
  let tribute;

  try {
    const response = await axios.get(url, {
        params: {
          object_pk: $commentsForm.data("object-pk"),
          content_type: $commentsForm.data("content-type"),
        },
      }
    );

    let values = [];
    for (const index in response.data.result) {
      const userValue = response.data.result[index];
      values.push({
        key: userValue.user_name,
        value: userValue.user_name,
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

async function getEmojiTribute($commentsForm) {
  const url = 'https://api.github.com/emojis';
  let tribute;

  try {
    const response = await axios.get(url);

    let values = [];
    for (const key in response.data) {
      const value = response.data[key];
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

function setupComment() {
  $(function () {
    const $commentsForm = $(".ab-comments-form");
    if (!$commentsForm.length) return;

    const editorTextArea = document.getElementById("id_comment");

    getEmojiTribute($commentsForm).then(function(tribute) {
      if (tribute) {
        tribute.attach(editorTextArea);
      }
    });

    getMentionTribute($commentsForm).then(function(tribute) {
      if (tribute) {
        tribute.attach(editorTextArea);
      }
    });

  });
}

export { setupComment };
