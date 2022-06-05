<template>
    <div class="list-wrapper">
        <h2>Projects</h2>
        <table id="projects-list-table" class="table table-hover">
        <thead class="table-dark">
            <tr>
                <th scope="col">Name</th>
                <th scope="col"># of Vertices</th>
                <th scope="col"># of Edges</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(project, index) in projectsList" :key="index" @click="openProject(project)">
                <td>
                    <span>{{ project.name }}</span>
                </td>
                <td>
                    <span>{{ JSON.parse(project.vertices).length }}</span>
                </td>
                <td>
                    <span>{{ JSON.parse(project.edges).length }}</span>
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
    // this lifecycle hook is called as Vue creates this component
    // this way the data will be available as the component reenders
    beforeCreate() {
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
        // given the project this stores project data locally and redirects
        openProject(project) {
            localStorage.setItem('vrtxList', project.vertices)
            localStorage.setItem('edgeList', project.edges)
            localStorage.setItem('result', project.result)
            localStorage.setItem('tree_id', project.id)
            localStorage.setItem('project_name', project.name)
            this.$router.push({ name: 'Home' })
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

tr {
    padding: 10px 0;
    font-size: larger;
}
</style>