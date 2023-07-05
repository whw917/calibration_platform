<style>
.template {
    width: 1400px;
    height: 100%;
}

.rate-demo {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.div-modal-content {
    width: 900px;
    height: 500px;
}
.col-caption{
    margin: 5px;
    color:chocolate;
}
.col-caption-upload{
    margin: 5px;
    color:blue;
}
</style>
<template class="template" >
    <Modal v-model="modal" title="传感器管理" width="1080" @on-ok="ok" @on-cancel="cancel">
        <div class="div-modal-content">
            <Card :bordered="false">
                <template #title>
                    <Row>
                        <i-Col span="4" class="col-caption"><span>传感器表</span></i-Col>
                        <i-Col span="12" class="col-caption-upload">
                            <span>导入传感器表</span>
                            <input class="upload_button" type='file' id='fileLabel' ref='upload' title='请上传xls或者xlsx格式文件'
                                accept='.xls, .xlsx' />
                        </i-Col>

                    </Row>
                </template>
                <Table width="90%" border :columns="sensorColumns" :data="expertPageList">

                </Table>
                <Page class="pageBox" style="margin-top: 30px;text-align: center" :total="pageInfo.pageTotal"
                    :current="pageInfo.page" :page-size="pageInfo.limit" @on-change="changePage" />
            </Card>
        </div>

    </Modal>
</template>
<script>
import ExcelUtils from "@/js/excel.js"
function setOptions(section, option_name, option_value, callback) {
    pywebview.api.setOptions(section, option_name, option_value).then(res => {
        // alert(res)
        // let jsonRsult = JSON.parse(res)
        callback(res)
    })
}


function setSensorList(rows, callback) {
    pywebview.api.setSensorList(rows).then(res => {
        // alert(res)
        // let jsonRsult = JSON.parse(res)
        callback(res)
    })
}


export default {
    name: 'SensorManagement',
    props: {
        visible: {
            type: Boolean,
            default: false,
        },
        modalShow: {
            type: Boolean,
            default: false,
        },
        id: {
            type: String,
            default: "",
        },
    },
    watch: {
        // 'visible': function (val, oldVal) {
        //     if (val != oldVal) {
        //         this.modal = val
        //     }
        // },

        'modalShow': function (val, oldVal) {
            if (val != oldVal) {
                this.modal = val
            }
        },
    },
    data() {
        return {
            modal: true,
            serialList: [
                {
                    name: 'COM10',
                    title: 'COM10'
                },
                {
                    name: 'COM11',
                    title: 'COM11'
                }

            ],
            comAngulayEncoder: "",
            comStepMotor: "",
            movieList: [
                {
                    name: 'The Shawshank Redemption',
                    url: 'https://movie.douban.com/subject/1292052/',
                    rate: 9.6
                },
                {
                    name: 'Leon:The Professional',
                    url: 'https://movie.douban.com/subject/1295644/',
                    rate: 9.4
                },
                {
                    name: 'Farewell to My Concubine',
                    url: 'https://movie.douban.com/subject/1291546/',
                    rate: 9.5
                },
                {
                    name: 'Forrest Gump',
                    url: 'https://movie.douban.com/subject/1292720/',
                    rate: 9.4
                },
                {
                    name: 'Life Is Beautiful',
                    url: 'https://movie.douban.com/subject/1292063/',
                    rate: 9.5
                },
                {
                    name: 'Spirited Away',
                    url: 'https://movie.douban.com/subject/1291561/',
                    rate: 9.2
                },
                {
                    name: 'Schindler\'s List',
                    url: 'https://movie.douban.com/subject/1295124/',
                    rate: 9.4
                },
                {
                    name: 'The Legend of 1900',
                    url: 'https://movie.douban.com/subject/1292001/',
                    rate: 9.2
                },
                {
                    name: 'WALL·E',
                    url: 'https://movie.douban.com/subject/2131459/',
                    rate: 9.3
                },
                {
                    name: 'Inception',
                    url: 'https://movie.douban.com/subject/3541415/',
                    rate: 9.2
                }
            ],
            randomMovieList: [],

            sensorColumns: [
                // {
                //     type: 'selection',
                //     width: 60,
                //     align: 'center',
                //     fixed: "left",
                // },
                {
                    title: "序号",
                    key: "id",
                    width: 100,
                },
                {
                    title: "传感器编号",
                    key: "sensorCode",
                    // width: 200,
                },
                {
                    title: "端口",
                    key: "sensorCom",
                    // width: 200,
                },
                {
                    title: "地址",
                    key: "sensorAddr",
                    // width: 150,
                },
                {
                    title: "传感器类型",
                    key: "sensorType",
                    // width: 200,
                },
                {
                    title: "通道",
                    key: "channel",
                    // width: 200,
                },

            ],
            pageInfo: {
                limit: 5,
                pageTotal: 1,
                page: 1
            },
            sensorList: [],
            expertPageList: [
                // {
                //     id: "1",
                //     sensorCode: "91002300",
                //     sensorCom: "COM20",
                //     sensorAddr: "1",
                //     sensorType: "35",
                //     channel: "1"
                // }
            ],
            sensor_rows : []
        }
    },
    created() {
        console.log("serial config")
    },
    mounted() {
        this.changeLimit();
        let that = this
        this.$refs.upload.addEventListener('change', e => {
            // 表格导入
            const files = e.target.files
            if (files.length <= 0) {
                // 如果没有文件名
                this.$Message.info("没有选择数据文件")
            } 
            else{
                let excelFile = files[0]
                document.getElementById('fileLabel').title = files[0].name
                ExcelUtils.load(excelFile, result=>{                
                that.$refs.upload.value = ''
                if( result.code == 0 ){
                    that.sensorList = result.sensorList
                    that.pageInfo.pageTotal = result.sensorList.length
                    that.$refs.upload.value = ''
                    that.changePage(1)
                }
            })
            }
            
            
        })
    },
    methods: {
        init(lstSerial) {
            this.serialList = lstSerial
        },
        changeLimit() {
            function getArrayItems(arr, num) {
                const temp_array = [];
                for (let index in arr) {
                    temp_array.push(arr[index]);
                }
                const return_array = [];
                for (let i = 0; i < num; i++) {
                    if (temp_array.length > 0) {
                        const arrIndex = Math.floor(Math.random() * temp_array.length);
                        return_array[i] = temp_array[arrIndex];
                        temp_array.splice(arrIndex, 1);
                    } else {
                        break;
                    }
                }
                return return_array;
            }
            this.randomMovieList = getArrayItems(this.movieList, 5);
        },
        ok() {     
            let rows = []
            this.sensorList.filter( e=>{
                let row=[]
                row.push(e.id)                
                row.push(e.sensorCode)         
                row.push(e.sensorCom)        
                row.push(e.sensorAddr)          
                row.push(e.sensorType)  
                row.push(e.channel)
                rows.push(row)
            })
            let strRows = JSON.stringify(rows)
            setSensorList(strRows, res=>{
                console.log(res)
            })      
            this.$emit("onClickOk")
            

        },
        cancel() {
            this.$emit("onClickCancel")
        },

        changePage(val) {
            this.pageInfo.page = val
            if (this.pageInfo.page <= 0) {
                this.pageInfo.page = 1
            }
            let rowStart = this.pageInfo.page * this.pageInfo.limit - this.pageInfo.limit;
            let rowEnd = this.pageInfo.page * this.pageInfo.limit;
            let that = this
            this.expertPageList = []
            for (var i = rowStart; i < that.sensorList.length && i < rowEnd; i++) {
                that.expertPageList.push(that.sensorList[i])
            }
        },
        // end of method
    },

}
</script>
