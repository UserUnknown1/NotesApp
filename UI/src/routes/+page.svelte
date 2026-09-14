<script>
    import { goto } from "$app/navigation";
import { json } from "@sveltejs/kit";
    import { onMount } from "svelte";

    let welcome=$state("My Notes App")
    let subtitle="Your comfy corner for all errant thoughts"
    
    let allNotes=$state([])
    onMount(async()=>{
    let response= await fetch("http://127.0.0.1:8000/api/notes/")
    let  newNote=await response.json()
    allNotes=newNote
    }  )
    let delNote = async (id) => {
    let response = await fetch(`http://127.0.0.1:8000/api/notes/${id}`, {
        method: "DELETE"
    })

    if (response.ok) {
        allNotes = allNotes.filter(note => note.id !== id)
    }
}

    let editNote=(id)=>{goto(`/put/${id}`)}
</script>
<div class="page">
<h1>
    {welcome}
</h1>
<h2>{subtitle}</h2>
<div>
   <div>
    <h3>All Notes</h3>
   
    </div>
    
</div>

<div>
    <p>All Notes</p>
    <table>
        <tbody>
        {#each allNotes as note}
        
        <tr>
            <td>{note.title}</td>
            <td>{note.content}</td>
            <td><button onclick={()=>editNote(note.id)}>Edit</button></td> 
            <td><button onclick={()=>delNote(note.id)}>Delete</button></td> 
        </tr>
        {/each}
        </tbody>
    </table>
    <div class="add-button">
    <button onclick={() => goto('/add')}>Add Note</button>
    </div>
    </div>
    </div>


    <style>
        h1{
            background-color: azure;
            color: hotpink;
            text-align: center;
            margin-bottom: 5px;
            font-weight: 600;
        }
        h2{
            background-color: azure;
            color: pink;
            text-align: center;
            margin-top: 5px;
            font-size: 20px;

        }
        h3{
            background-color: azure;
            color: hotpink;
            text-align: center;
            font-weight: 600;
            font-size: 24px

        }
        .page{
            background-color: #160b1f;
            min-height: 100vh;
        }
        .add-button{
            text-align: center;
        }
    </style>