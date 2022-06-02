<template>
    <form @submit.prevent="">
        <h2 >All Vertices</h2>
        <table id="vrtx-list-table" class="table table-hover">
            <thead class="table-dark">
                <tr>
                    <th scope="col">ID</th>
                    <th scope="col">Name</th>
                    <th scope="col">Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(vrtx, index) in vrtxList" :key="index">
                    <td>
                        <span v-show="!vrtx.inEditMode">{{ vrtx.vrtxID }}</span>
                        <input type="number" v-bind:placeholder="vrtx.vrtxID" v-show="vrtx.inEditMode" v-model="vrtx.vrtxID" /> 
                    </td>
                    <td>
                        <span v-show="!vrtx.inEditMode">{{ vrtx.vrtxName }}</span>
                        <input v-bind:placeholder="vrtx.vrtxName" v-show="vrtx.inEditMode" v-model="vrtx.vrtxmName" />
                    </td>
                    <td>
                        <button type="button" class="btn btn-success" v-show="vrtx.inEditMode" @click="editVrtxComplete(vrtx)"><i class="fa fa-save"></i>Save</button>
                        <button type="button" class="btn btn-primary" v-show="!vrtx.inEditMode" @click="editVrtx(vrtx)"><i class="fa fa-edit"></i>Edit</button>
                        <button type="button" class="btn btn-danger" @click="removeVrtx(index)"><i class="fa fa-remove"></i>Delete</button>
                    </td>
                </tr>
            </tbody>
        </table>
        <div class="addnewvrtx-wrapper">
            <h4>Add new Vertex to your Spanning Tree</h4>
            <div class="row justify-content-around">
                <div class="col-4 form-group ">
                    <label for="vrtxID">ID</label>
                    <input type="number" v-model="vrtxID" autofocus>
                </div>
                <div class="col-4 form-group">
                    <label for="vrtxName">Name</label>
                    <input type="text" v-model="vrtxName">
                </div>
                <button type="button" @click="addVrtx" class="col-2 btn btn-primary" ><i class="fa fa-plus"></i>Add</button>
            </div>
        </div>
    </form>
</template>


<script>
export default {
    name: "addVrtxList",
    data() {
        return {
            vrtxID: '',
            vrtxName: '',
            inEditMode: false,
            vrtxList: [
                {vrtxID: 1, vrtxName: 'A', inEditMode: false},
                {vrtxID: 2, vrtxName: 'B', inEditMode: false},
            ]
        }
    },
    methods: {
        addVrtx(){
            var inputVrtxID = this.vrtxID
            var inputVrtxName = this.vrtxName.trim()
            this.vrtxList.push({ 
            vrtxID: inputVrtxID,
            vrtxName: inputVrtxName,
            inEditMode: false
            });
            this.clearAll()
        },
        clearAll() {
        this.vrtxID += 1
        this.vrtxName = ''
        },
        removeVrtx(index){
            this.vrtxList.splice(index, 1) //delete 1 element from the array at the position index
        },
        editVrtx:function (vrtx){
            vrtx.inEditMode = true
        },
        editVrtxComplete: function (vrtx) {
            vrtx.inEditMode = false
        }
    }
}
</script>


<style scoped>
#vrtx-list-table{
  table-layout: fixed;
  vertical-align: middle;
}

button {
  margin-left: 12px;
}

.addnewvrtx-wrapper {
    width: 75%;
    background-color: rgb(223, 223, 223);
    margin: 5px;
    padding: 10px;
    border-radius: 5px;
}
</style>