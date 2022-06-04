<template>
    <div class="list-wrapper">
        <h2>Projects</h2>
        <table id="projects-list-table" class="table table-hover">
        <thead class="table-dark">
            <tr>
                <th scope="col">Name</th>
                <th scope="col">last modified</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(project, index) in projectList" :key="index" @click="openProject(project)">
                <td>
                    <span>{{ project.name }}</span>
                </td>
                <td>
                    <span>{{ project.last_modified }}</span>
                </td>
            </tr>
        </tbody>
    </table>
    </div>
</template>


<script>
import axios from 'axios'

export default {
    name: "AllProjects",
    created() {
        axios.get(`getUserTrees/${parseInt(localStorage.getItem('user_id'))}`).then( response => {
            if (response.status === 200) {
                this.projectsList = response.data.projects
            }
        }).catch( err => {
            console.log("error:", err)
        })
    },
    data() {
        return {
            projectsList: []
        }
    },
    methods: {
        openProject() {

        }
    },
}
</script>


<style scoped>
h2 {
    font-weight: bold;
}

#project-list-table{
  table-layout: fixed;
  vertical-align: middle;
}

</style>