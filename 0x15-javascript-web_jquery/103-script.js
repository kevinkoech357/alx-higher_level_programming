$(document).ready(function () {
  $('#btn_translate, #language_code').on('click keypress', function (e) {
    if (e.type === 'click' || (e.type === 'keypress' && e.which === 13)) {
      const languageCode = $('#language_code').val();
      const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;

      $.ajax({
        url: apiUrl,
        success: function (data) {
          $('#hello').text(data.hello);
        },
        error: function () {
          $('#hello').text('Translation not found');
        }
      });
    }
  });
});
