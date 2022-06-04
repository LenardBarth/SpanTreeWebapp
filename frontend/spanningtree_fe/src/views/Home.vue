<template>
<div class="content-wrapper">
    <div class="component-wrapper">
        <addVrtxListVue @infoPopup="$emit('infoPopup', $event)" @changeVrtxList="passListChanged()"/>
    </div>
    <div class="component-wrapper">
        <addEdgeListVue @infoPopup="$emit('infoPopup', $event)" :newVrtxList="changedList"/>
    </div>
</div>
<div class="send-wrapper">
    <button class="btn btn primary btn-success btn-lg" @click="sendTree()">Submit Spanning Tree to Compute</button>
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
            const response = await axios.post('computeTree', payload)
            console.log("response", response);
        }
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

.send-wrapper {
    margin: 50px auto;
}
</style>