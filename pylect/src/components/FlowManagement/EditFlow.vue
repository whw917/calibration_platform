<style scoped>


.page-bar{
    text-align:right;
    margin-top: 20px;
}

</style>

<template>
    <div >
        <Input v-model="queryParam.name" placeholder="name" clearable size="large" />

    </div>
</template>
  
  <script>
  import { Row, Input, Button, Table, Page, Space, FormItem, resolveComponent} from 'view-design'
  
  export default {
    components: {
    Input,
    Button,
    Table,
    Page,
    Space,
    FormItem,
    Row
},

    data() {
        return {
            queryParam: {
                name: '',
                
            },
        }
        },
        methods: {

        }

  }
  </script>