<style scoped>

.title {
    font-size: 1em;
    text-align: left;
    margin-bottom: 20px;
    margin-left: 5px;
  }

.table-page{
    width: 80%;
    margin: auto;
}
</style>

<template>
    <div>
        <h2 class="title">参数设置</h2>

            <div class="table-page">
                <Parametertable/>
            </div>   

  
    </div>
  </template>
  
  <script>
  import { Input, Button, Table, Page, Space, model, FormItem} from 'view-design'
  import Parametertable from './Parametertable.vue'

  export default {
    components: {
      Input,
      Button,
      Table,
      Page,
      FormItem,

      Parametertable,

    },

  }
  </script>