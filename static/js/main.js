const btn_delete = document.querySelectorAll('.btn-delete')
if (btn_delete){
    const btn_delete_array = Array.from(btn_delete);
    btn_delete_array.forEach((btn_del)=>{
        btn_del.addEventListener('click',(e)=>{
            if(!confirm('¿Estas seguro de querer eliminar?')){
                e.preventDefault();
            }
        })
    })
}

const btn_update = document.querySelectorAll('.btn-update')
if (btn_update){
    const btn_update_array = Array.from(btn_update);
    btn_update_array.forEach((btn_up)=>{
        btn_up.addEventListener('click',(e)=>{
            if(!confirm('¿Los datos son correctos?')){
                e.preventDefault();
            }
        })
    })
}