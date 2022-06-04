<template>
    <!-- List Layout and Funcionalty from https://codepen.io/SimoTuognia/pen/ZjYJQo -->
    <form @submit.prevent="">
        <h2 >Edges</h2>
        <div class="addnewedge-wrapper">
            <h4>Add new edge between two vertices</h4>
            <div class="row justify-content-start">
                <div class="col col-4 form-group ">
                    <label class="w-100" for="from">From</label>
                    <select class="vrtx-select" v-model="From" required>
                        <option id="default" disabled value="">- From Vertex -</option>
                        <option v-for="(vrtx, index) in vrtxList" :key="index"></option>
                    </select>
                </div>
                <div class="col col-4 form-group">
                    <label class="w-100" for="To">To</label>
                    <select class="vrtx-select" v-model="To" required>
                        <option id="default" disabled value="">- To Vertex -</option>
                        <option v-for="(vrtx, index) in vrtxList" :key="index"></option>
                    </select>
                </div>
                <div class="col col-4 form-group">
                    <label class="w-100" for="Weight">Weight</label>
                    <input type="number" v-model="Weight">
                </div>
            </div>
            <button type="button" @click="addEdge" class="btn btn-primary" ><i class="fa fa-plus"></i>Add</button>
        </div>
        <table id="edge-list-table" class="table table-hover">
            <thead class="table-dark">
                <tr>
                    <th scope="col">From</th>
                    <th scope="col">To</th>
                    <th scope="col">Weight</th>
                    <th scope="col">Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(edge, index) in edgeList" :key="index">
                    <td>
                        <span v-show="!edge.inEditMode">{{ edge.From }}</span>
                        <select class="vrtx-select" v-model="From" v-show="edge.inEditMode" required>
                            <option id="default" disabled value="">- From Vertex -</option>
                            <option v-for="(vrtx, index) in vrtxList" :key="index"></option>
                        </select>
                    </td>
                    <td>
                        <span v-show="!edge.inEditMode">{{ edge.To }}</span>
                        <select class="vrtx-select" v-model="To" v-show="edge.inEditMode" required>
                            <option id="default" disabled value="">- To Vertex -</option>
                            <option v-for="(vrtx, index) in vrtxList" :key="index"></option>
                        </select>
                    </td>
                    <td>
                        <span v-show="!edge.inEditMode">{{ edge.Weight }}</span>
                        <input v-bind:placeholder="edge.Weight" v-show="edge.inEditMode" v-model="edge.Weight" />
                    </td>
                    <td>
                        <button type="button" class="btn btn-success" v-show="edge.inEditMode" @click="editEdgeComplete(edge)"><i class="fa fa-save"></i>Save</button>
                        <button type="button" class="btn btn-primary" v-show="!edge.inEditMode" @click="editEdge(edge)"><i class="fa fa-edit"></i>Edit</button>
                        <button type="button" class="btn btn-danger" @click="removeVrtx(index)"><i class="fa fa-remove"></i>Delete</button>
                    </td>
                </tr>
            </tbody>
        </table>
        
    </form>
</template>


<script>
export default {
    name: "addEdgeList",
    data() {
        return {
            From: '',
            To: '',
            Weight: '',
            inEditMode: false,
            edgeList: [
                {From: 'A', To: 'B', Weight: 5, inEditMode: false},
            ],
            vrtxList: []
        }
    },
    methods: {
        addEdge(){
            var inputFrom = this.From.trim()
            var inputTo = this.To.trim()
            var inputWeight = this.Weight
            this.edgeList.push({ 
                From: inputFrom,
                To: inputTo,
                Weight: inputWeight,
                inEditMode: false
            });
            this.clearAll()
        },
        clearAll() {
            this.From = ''
            this.To = ''
            this.Weight = ''
        },
        removeEdge(index){
            this.EdgeList.splice(index, 1) //delete 1 element from the array at the position index
        },
        editEdge(edge){
            edge.inEditMode = true
        },
        editEdgeComplete(edge) {
            edge.inEditMode = false
        }
    }
}
</script>


<style scoped>
#edge-list-table{
  table-layout: fixed;
  vertical-align: middle;
}

.addnewedge-wrapper button {
  width: 80%;
  margin-top: 10px;
}

table button {
  margin: 0 6px;
}

.addnewedge-wrapper {
    height: 150px;
    width: 95%;
    background-color: rgb(223, 223, 223);
    margin: 10px;
    padding: 5px;
    border-radius: 5px;
}

input, select {
    width: 80%;
}

.col.col-2.form-group, .col.col-4.form-group {
    padding: 0;
}
</style>