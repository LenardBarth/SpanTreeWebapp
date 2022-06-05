<template>
    <!-- List Layout and Funcionalty from https://codepen.io/SimoTuognia/pen/ZjYJQo -->
    <h2 >Vertices</h2>
    <div class="addnewvrtx-wrapper">
        <form @submit.prevent="">
            <h4>Add new Vertex to your Spanning Tree</h4>
            <div class="row justify-content-around">
                <div class="col col-4 form-group ">
                    <label class="w-100" for="vrtxID">ID</label>
                    <input type="number" v-model="vrtxID" min="1">
                </div>
                <div class="col col-4 form-group">
                    <label class="w-100" for="vrtxName">Name</label>
                    <input type="text" v-model="vrtxName">
                </div>
            </div>
            <button type="button" @click="addVrtx" class="btn btn-primary" ><i class="fa fa-plus"></i>Add</button>
        </form>
    </div>
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
                    <span>{{ vrtx.vrtxID }}</span>
                </td>
                <td>
                    <span>{{ vrtx.vrtxName }}</span>
                </td>
                <td>
                    <button type="button" class="btn btn-danger" @click="removeVrtx(index)"><i class="fa fa-remove"></i>Delete</button>
                </td>
            </tr>
        </tbody>
    </table>
</template>


<script>
import axios from 'axios'

export default {
    name: "addVrtxList",
    emits: ['infoPopup', 'changeVrtxList'],
    created() {
    },
    data() {
        return {
            vrtxID: '',
            vrtxName: '',
            vrtxList: localStorage.getItem('vrtxList')===null ? [] : JSON.parse(localStorage.getItem('vrtxList'))
        }
    },
    methods: {
        addVrtx(){
            // since form never gets submitted 'required' attribute on input does not work
            // therefore check if input is complete via if(..)
            if (!isNaN(this.vrtxID) && this.vrtxName !== "") {
                var inputVrtxID = this.vrtxID
                var inputVrtxName = this.vrtxName.trim()
                // vertex with specified data is pushed to component-internal list of all vertices
                this.vrtxList.push({ 
                    vrtxID: inputVrtxID,
                    vrtxName: inputVrtxName
                })
                // update list of all vertices with newly added vertex (stored in browser localStorage)
                localStorage.setItem('vrtxList', JSON.stringify(this.vrtxList))
                this.clearAll()
                this.$emit('changeVrtxList')
            } else {
                this.$emit('infoPopup', {status: "info", msg: "Please enter ID and Name"})
            }
        },
        // resets all inputs to empty
        clearAll() {
            this.vrtxID = parseInt(this.vrtxID) + 1
        this.vrtxName = ''
        },
        // removes vertex from list of all vertices
        removeVrtx(index){
            this.vrtxList.splice(index, 1)  //delete 1 element from the array at the position index
            localStorage.setItem('vrtxList', JSON.stringify(this.vrtxList))
            this.$emit('changeVrtxList')
        }
    }
}
</script>


<style scoped>
h2 {
    font-weight: bold;
}

#vrtx-list-table{
  table-layout: fixed;
  vertical-align: middle;
}

.addnewvrtx-wrapper button {
  width: 80%;
  margin-top: 10px;
}

table button {
  margin: 0 6px;
}

.addnewvrtx-wrapper {
    height: 150px;
    width: 95%;
    background-color: rgb(223, 223, 223);
    margin: 10px;
    padding: 5px;
    border-radius: 5px;
}

input {
    width: 70%;
}
</style>