const formSubmit = (evt) => {
    evt.preventDefault()
    const formData = new FormData(evt.target)
    console.log(formData)
    const formProps = Object.fromEntries(formData)
    console.log(formProps)
    let p_tags = document.querySelectorAll("p")
    p_tags[0].innerText += ' ' +formProps['first']
    p_tags[1].innerText += ' ' +formProps['last']
}
