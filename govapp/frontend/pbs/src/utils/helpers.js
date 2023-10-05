module.exports = {
    formatError: function (err) {
        let returnStr = '';
        // object {}
        if (
            typeof err.body === 'object' &&
            !Object.prototype.hasOwnProperty.call(err.body, 'length')
        ) {
            for (const key of Object.keys(err.body)) {
                returnStr += `${key}: ${err.body[key]} <br/>`;
            }
            // array
        } else if (typeof err.body === 'object') {
            returnStr = err.body[0];
            // string
        } else {
            returnStr = err.body;
        }
        return returnStr;
    },
    formatErrorV2: function (errors) {
        if (typeof errors === 'string') {
            return errors;
        }
        if (Array.isArray(errors)) {
            if (1 == errors.length) {
                return errors[0];
            } else {
                let errors_str = '';
                for (let i = 0; i < errors.length; i++) {
                    errors_str += errors[i] + '<br/>';
                }
                return errors_str;
            }
        }
        if (typeof errors === 'object') {
            if (1 == Object.keys(errors).length) {
                return Object.values(errors)[0];
            } else {
                let errors_str = '<ul class="list-group text-start">';
                for (const key of Object.keys(errors)) {
                    errors_str += `<li class="list-group-item"><span class="fw-bold">${key}:</span> ${module.exports.escapeHtml(
                        errors[key]
                    )}</li>`;
                }
                return errors_str + '</ul>';
            }
        }
    },
    escapeHtml: function (htmlStr) {
        return htmlStr
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#39;');
    },
    getCookie: function (name) {
        var value = null;
        if (document.cookie && document.cookie !== '') {
            let cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                let cookie = cookies[i].trim();
                if (
                    cookie.substring(0, name.length + 1).trim() ===
                    name + '='
                ) {
                    value = decodeURIComponent(
                        cookie.substring(name.length + 1)
                    );
                    break;
                }
            }
        }
        return value;
    },
    add_endpoint_join: function (api_string, addition) {
        // assumes api_string has trailing forward slash '/' character required for POST
        let endpoint = api_string + addition;
        endpoint = endpoint.replace('//', '/'); // Remove duplicated '/' just in case
        // if the last character is not a forward slash then add one
        if (endpoint.slice(-1) != '/') {
            endpoint += '/';
        }
        return endpoint;
    },
    enablePopovers: function () {
        let popoverTriggerList = [].slice.call(
            document.querySelectorAll('[data-bs-toggle="popover"]')
        );
        popoverTriggerList.map(function (popoverTriggerEl) {
            new bootstrap.Popover(popoverTriggerEl); // eslint-disable-line no-undef
        });
    },
    getFileIconClass: function (filepath, additional_class_names = []) {
        let ext = filepath.split('.').pop().toLowerCase();
        let classname = additional_class_names;

        if (['png', 'jpg', 'jpeg', 'bmp', 'tiff', 'tif'].includes(ext)) {
            classname.push('bi-file-image-fill');
        } else if (['pdf'].includes(ext)) {
            classname.push('bi-file-pdf-fill');
        } else if (['doc', 'docx'].includes(ext)) {
            classname.push('bi-file-word-fill');
        } else if (['xls', 'xlsx'].includes(ext)) {
            classname.push('bi-file-excel-fill');
        } else if (['txt', 'text'].includes(ext)) {
            classname.push('bi-file-text-fill');
        } else if (['rtf'].includes(ext)) {
            classname.push('bi-file-richtext-fill');
        } else if (['mp3', 'mp4'].includes(ext)) {
            classname.push('bi-file-play-fill');
        } else {
            classname.push('bi-file_fill');
        }

        return classname.join(' ');
    },
    formatDateForAPI: function (data, format = 'DD/MM/YYYY') {
        return data ? moment(data).format(format) : ''; // eslint-disable-line no-undef
    },
};