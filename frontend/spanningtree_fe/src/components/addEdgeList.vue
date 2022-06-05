<template>
    <!-- List Layout and Funcionalty from https://codepen.io/SimoTuognia/pen/ZjYJQo -->
    <h2 >Edges</h2>
    <div class="addnewedge-wrapper">
        <form @submit.prevent="">
            <h4>Add new edge between two vertices</h4>
            <div class="row justify-content-start">
                <div class="col col-4 form-group ">
                    <label class="w-100" for="from">From</label>
                    <select class="vrtx-select" v-model="From">
                        <option id="default" disabled value="">- From Vertex -</option>
                        <option v-for="(vrtx, index) in getVrtcs()" :key="index" :value="vrtx.vrtxName">{{ vrtx.vrtxName }}</option>
                    </select>
                </div>
                <div class="col col-4 form-group">
                    <label class="w-100" for="To">To</label>
                    <select class="vrtx-select" v-model="To">
                        <option id="default" disabled value="">- To Vertex -</option>
                        <option v-for="(vrtx, index) in getVrtcs()" :key="index" :value="vrtx.vrtxName">{{ vrtx.vrtxName }}</option>
                    </select>
                </div>
                <div class="col col-4 form-group">
                    <label class="w-100" for="Weight">Weight</label>
                    <input type="number" v-model="Weight" min="1">
                </div>
            </div>
            <button type="submit" @click="addEdge" class="btn btn-primary" ><i class="fa fa-plus"></i>Add</button>
        </form>
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
                    <span>{{ edge.From }}</span>
                </td>
                <td>
                    <span>{{ edge.To }}</span>
                </td>
                <td>
                    <span>{{ edge.Weight }}</span>
                </td>
                <td>
                    <button type="button" class="btn btn-danger" @click="removeEdge(index)"><i class="fa fa-remove"></i>Delete</button>
                </td>
            </tr>
        </tbody>
    </table>
</template>


<script>
export default {
    name: "addEdgeList",
    emits: ['infoPopup'],
    props: ['newVrtxList'],
    watch: {
        newVrtxList() {
            this.vrtxList = localStorage.getItem('vrtxList')===null ? [] : JSON.parse(localStorage.getItem('vrtxList'))
        }
    },
    created() {
    },
    data() {
        return {
            From: '',
            To: '',
            Weight: '',
            edgeList: localStorage.getItem('edgeList')===null ? [] : JSON.parse(localStorage.getItem('edgeList')),
            vrtxList: localStorage.getItem('vrtxList')===null ? [] : JSON.parse(localStorage.getItem('vrtxList'))
        }
    },
    methods: {
        addEdge(){
            if (this.From.valueOf()!=="" && this.From.valueOf()!=="" && !isNaN(this.Weight)) {
                const inputFrom = this.From.valueOf()
                const inputTo = this.To.valueOf()
                const inputWeight = this.Weight
                this.edgeList.push({ 
                    From: inputFrom,
                    To: inputTo,
                    Weight: inputWeight
                })
                localStorage.setItem('edgeList', JSON.stringify(this.edgeList))
                this.clearAll()
            } else {
                this.$emit('infoPopup', {status: "info", msg: "Please fill in both vertices and the corresponding wheight"})
            }
        },
        clearAll() {
            this.From = ''
            this.To = ''
            this.Weight = ''
        },
        removeEdge(index){
            this.edgeList.splice(index, 1)  //delete 1 element from the array at the position index
            localStorage.setItem('edgeList', JSON.stringify(this.edgeList))
        },
        getVrtcs() {
            return this.vrtxList
        }
    }
}
</script>


<style scoped>
h2 {
    font-weight: bold;
}

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

select {
    height: 30px;
    padding: 1px 2px;
}

.col.col-2.form-group, .col.col-4.form-group {
    padding: 0;
}
</style>