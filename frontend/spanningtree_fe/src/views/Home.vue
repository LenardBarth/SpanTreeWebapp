<template>
<div class="content-wrapper">
    <div class="component-wrapper">
        <addVrtxListVue @infoPopup="$emit('infoPopup', $event)" @changeVrtxList="passListChanged()"/>
    </div>
    <div class="component-wrapper">
        <addEdgeListVue @infoPopup="$emit('infoPopup', $event)" :newVrtxList="changedList"/>
    </div>
</div>
<div class="wrapper">
    <div class="form-group">
        <label for="project_name">Name of project</label><br>
        <input type="text" name="project_name" id="project_name" v-model="project_name" :placeholder="project_name===''?'Choose Name':project_name">
    </div>
    <div class="btn-wrapper">
        <button class="btn btn-outline-primary btn-lg" @click="saveTree()">Save</button>
    </div>
    <div class="btn-wrapper">
        <button class="btn btn-success btn-lg" @click="sendTree()">Submit Spanning Tree to Compute</button>
    </div>
</div>
</template>

<script>
import addVrtxListVue from '@/components/addVrtxList.vue'
import addEdgeListVue from '@/components/addEdgeList.vue'
import axios from 'axios'

export default {
    name: "HomePage",
    emits: ['infoPopup'],
    components: {
        addVrtxListVue,
        addEdgeListVue
    },
    data() {
        return {
            changedList: [],
            project_name: localStorage.getItem('project_name')
        }
    },
    methods: {
        // passes a updated list from one component to another as they cannot detect updates in localStorage
        passListChanged() {
            this.changedList = JSON.parse(localStorage.getItem('vrtxList'))
        },
        // sends Spanning Tree data to backend to be processed and receives result lsit in return (in case of error result will be empty)
        async sendTree() {
            // create data to be sent
            let payload = {
                'vrtcs': JSON.parse(localStorage.getItem('vrtxList')),
                'edges': JSON.parse(localStorage.getItem('edgeList'))
            }
            //send request to backend using axios
            const response = await axios.post('computeTree', payload).catch(err => {
                console.log(err)
                this.$emit('infoPopup', {status: "danger", msg: "Server error"})
            })
            // if request wass successful
            if (response && response.status === 200) {
                // if backend did not throw any errors
                if (response.data.status === 'success') {
                    localStorage.setItem('result', JSON.stringify(response.data.result))
                    this.$router.push({ name: 'Result'})
                }
                this.$emit('infoPopup', {status: response.data.status, msg: response.data.message})
            } else {
                this.$emit('infoPopup', {status: "danger", msg: "Could not reach Server"})
            }
        },
        // sends request to save data of Spanning Tree project user is currently working on
        async saveTree() {
            // make sure user is logged in, in order to save
            if (localStorage.getItem('logged_in')==="True"){
                // make sure project is not nameless
                if (this.project_name!==""){
                    // create data to be sent
                    let payload = {
                        'tree_id': localStorage.getItem('tree_id'),
                        'user_id': localStorage.getItem('user_id'),
                        'name': this.project_name,
                        'vrtcs': localStorage.getItem('vrtxList'),
                        'edges': localStorage.getItem('edgeList'),
                        'result': localStorage.getItem('result'),
                    }
                    const response = await axios.post('save', payload).catch(err => {
                        console.log(err)
                        this.$emit('infoPopup', {status: "danger", msg: "Server error while trying to save"})
                    })
                    // if request wass successful
                    if (response && response.status === 200) {
                        // if backend did not throw any errors
                        if (response.data.status === 'success') {
                            localStorage.setItem('tree_id', response.data.tree_id)
                        }
                        this.$emit('infoPopup', {status: response.data.status, msg: response.data.message})
                    } else {
                        this.$emit('infoPopup', {status: "danger", msg: "Could not be saved"})
                    }
                // if project is nameless
                } else {
                    this.$emit('infoPopup', {status: "info", msg: "You should give your project a name first"})
                }
            // if user is not logged in
            } else {
                this.$emit('infoPopup', {status: "info", msg: "You must be logged in to save"})
            }
        },
    }
}
</script>

<style scoped>
.content-wrapper {
    width: 100vw;
    display: flex;
    justify-content: space-between;
}
.component-wrapper {
    width: 50%;
    margin: 5px;
    background-color: rgb(236, 236, 236);
    border-radius: 5px;
    padding: 5px;
}

.component-wrapper:first-of-type {
    margin-right: 2px;
}

.component-wrapper:last-of-type {
    margin-left: 2px;
}


.wrapper {
    width: 60vw;
    background-color: rgb(236, 236, 236);
    padding: 15px;
    margin: 5px auto;
    border-radius: 5px;
}

.btn-wrapper {
    margin: 50px auto;
}
</style>