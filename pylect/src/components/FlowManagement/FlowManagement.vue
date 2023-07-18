<style scoped>

.title {
    font-size: 1em;
    text-align: left;
    margin-bottom: 20px;
    margin-left: 5px;
  }


.search-bar{
    width: 80%;
    margin: auto;
}

.table-page{
    width: 80%;
    margin: auto;
}

.left-function {
    margin-right: 10px; /* Adjust the value as per your preference */
  }
</style>

<template>
    <div>
        <h2 class="title">标定流程管理</h2>

        <Form class="search-form" ref="formRef" :model="queryParam"  >
            <Row class="search-bar" glutter="16">
                <!-- 查询 -->
                <Col span="7" align="left">
                    <FormItem >
                    <Input search v-model="queryParam.keyword" placeholder="请输入" style="width: 90%" />
                    </FormItem>
                </Col>

        
                <Col>
                    <Button type="primary" @click="searchQuery" icon="search">查询</Button>
                </Col>

                <Col align="right" offset="9">
                <Row >
                    <Col class="left-function">
                        <Button type="primary" @click="createNew" icon="search">新建</Button>
                    </Col>

                    <Col class="left-function">
                        <Upload action="//jsonplaceholder.typicode.com/posts/">
                            <Button icon="ios-cloud-upload-outline">上传文件</Button>
                        </Upload>
                    </Col>

                    <Col class="left-function">
                        <Button type="primary" @click="downloadTemp" icon="search">下载模版</Button>
                    </Col>
                </Row>
                </Col>

            </Row>

            <div class="table-page">
                <FlowTable ref="flowTable" />
            </div>   

        </Form>
  
    </div>
  </template>
  
  <script>
  import { Input, Button, Table, Page, Space, model, FormItem} from 'view-design'
  import FlowTable from './FlowTable.vue'

  export default {
    components: {
      Input,
      Button,
      Table,
      Page,
      FormItem,

      FlowTable,

    },
    flowData: [],
    data() {
        return {
            file: null,
            loadingStatus: false,
            isPyWebViewReady: false,
            queryParam: {
                keyword: '',
                column: '',
                orderBy: '',
            },
            
        }
    },
    
    
    methods :{
        searchQuery() {
            this.$refs.flowTable.fetchFlowData(this.queryParam);
            console.log(this.queryParam);
        },

        createNew(){
            console.log('creat new' );
            this.$router.push('/add-flow'); 
        },
        


        downloadTemp(){
            console.log('download template' )
        },
    }

  }


  </script>