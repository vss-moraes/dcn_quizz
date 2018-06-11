window.onload = () => {
    if (location.href.includes('/pergunta'))
        getCache();
}

const cacheForm = () => {
    localStorage.setItem('formData', JSON.stringify(formToJSON(document.forms[0], document.forms[0].elements)));
    location.href = '/categoria';
}

const getCacheForm = () => {
    const cache = JSON.parse(localStorage.getItem('formData'));
    if (cache != null) {
        const form = document.forms[0];
        let indexName = 0;
        for (input of form.elements) {
            input.value = cache[input.name]
        }
        localStorage.clear();
    }
}

const formToJSON = elements => [].reduce.call(elements, (data, element) => {
    data[element.name] = element.value;
    return data;

}, {});