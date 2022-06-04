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
            changedList: []
        }
    },
    methods: {
        passListChanged() {
            this.changedList = JSON.parse(localStorage.getItem('vrtxList'))
        },
        async sendTree() {
            let payload = {
                'vrtcs': JSON.parse(localStorage.getItem('vrtxList')),
                'edges': JSON.parse(localStorage.getItem('edgeList'))
            }
            const response = await axios.post('computeTree', payload).catch(err => {
                console.log(err)
                this.$emit('infoPopup', {status: "danger", msg: "Server error"})
            })
            if (response && response.status === 200) {
                console.log("response:", response);
                if (response.data.status === 'success') {
                    localStorage.setItem('result', toString(response.data.result))
                    // this.$router.push({ name: 'Result'})
                }
                this.$emit('infoPopup', {status: response.data.status, msg: response.data.message})
            } else {
                this.$emit('infoPopup', {status: "danger", msg: "Could not reach Server"})
            }
        },
        async saveTree() {
            if (localStorage.getItem('logged_in')==="True"){
                let payload = {
                    'tree_id': parseInt(localStorage.getItem('treeID')),
                    'vrtcs': localStorage.getItem('vrtxList'),
                    'edges': localStorage.getItem('edgeList'),
                    'result': localStorage.getItem('result')
                }
                const response = await axios.post('computeTree', payload).catch(err => {
                    console.log(err)
                    this.$emit('infoPopup', {status: "danger", msg: "Server error while trying to save"})
                })
                if (response && response.status === 200) {
                    console.log("response:", response)
                    this.$emit('infoPopup', {status: response.data.status, msg: response.data.message})
                } else {
                    this.$emit('infoPopup', {status: "danger", msg: "Could not be saved"})
                    }
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