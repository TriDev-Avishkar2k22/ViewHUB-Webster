const search = document.querySelector('.search')
      const btn = document.querySelector('.bot')
      const input = document.querySelector('.input')

      btn.addEventListener('click', () => {
          search.classList.toggle('active')
          input.focus()
      })
const data = "{{filter}}"
console.log(data)

const rdata = JSON.parse(data.replace(/&quot;/g, '"'))
console.log(rdata)
 const inp = document.getElementById('search-bar')
console.log(inp)


let filterItem = []
const box = document.getElementById('box')
inp.addEventListener('keyup', (e)=>{
  box.innerHTML = ""
  console.log(e.target.value)
  filterArr = rdata.filter(data=> data['fields'].includes(e.target.value))
  console.log(filterArr)
})