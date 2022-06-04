<template>
<div class="content-wrapper">
    <div class="component-wrapper">
        <addVrtxListVue @infoPopup="$emit('infoPopup', $event)" @changeVrtxList="passListChanged()"/>
    </div>
    <div class="component-wrapper">
        <addEdgeListVue @infoPopup="$emit('infoPopup', $event)" :newVrtxList="changedList"/>
    </div>
</div>
</template>

<script>
import addVrtxListVue from '@/components/addVrtxList.vue'
import addEdgeListVue from '@/components/addEdgeList.vue'

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
    width: 49%;
    margin: 5px;
}
</style>