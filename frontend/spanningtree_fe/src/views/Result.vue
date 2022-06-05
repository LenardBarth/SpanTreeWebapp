<template>
    <h2>Result{{ name }}</h2>
    <div class="result-wrapper">
        <div class="line-wrapper" v-for="(line, index) in results" :key="index">
            <span class="result-line">{{ line }}</span><br>
        </div>
    </div>
    <div class="d-flex justify-content-between">
        <div class="resume-wrapper" id="vertices-wrapper">
            <h4>Vertices</h4>
            <table id="vrtx-list-table" class="table table-hover">
                <thead class="table-dark">
                    <tr>
                        <th scope="col">ID</th>
                        <th scope="col">Name</th>
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

                    </tr>
                </tbody>
            </table>
        </div>
        <div class="resume-wrapper" id="edges-wrapper">
            <h4>Edges</h4>
            <table id="edge-list-table" class="table table-hover">
            <thead class="table-dark">
                <tr>
                    <th scope="col">From</th>
                    <th scope="col">To</th>
                    <th scope="col">Weight</th>

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
                </tr>
            </tbody>
        </table>
        </div>
    </div>
</template>


<script>
export default {
    name: "ResultView",
    emits: ['infoPopup'],
    data() {
        return {
            name: localStorage.getItem('project_name')===null?'':` of ${localStorage.getItem('project_name')}`,
            results: localStorage.getItem('result')===null ? [] : JSON.parse(localStorage.getItem('result')),
            edgeList: localStorage.getItem('edgeList')===null ? [] : JSON.parse(localStorage.getItem('edgeList')),
            vrtxList: localStorage.getItem('vrtxList')===null ? [] : JSON.parse(localStorage.getItem('vrtxList'))
        }
    }
    
}
</script>


<style scoped>
.resume-wrapper {
    width: 49%;
    margin: 5px;
    background-color: rgb(236, 236, 236);
    border-radius: 5px;
    padding: 5px;
}

.result-wrapper {
    margin: 5px;
    background-color: rgb(236, 236, 236);
    border-radius: 5px;
    padding: 20px;
}

.result-wrapper span {
    font-size: large;
}
</style>