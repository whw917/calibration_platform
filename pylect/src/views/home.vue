
<style scoped>
.layout {
  border: 1px solid #d7dde4;
  background: #f6f5ec;
  position: relative;
  border-radius: 4px;
  height: 100%;
  /* overflow: hidden; */
}

.layout-header-bar {
  background: #fff;
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.1);
}

.layout-logo-left {
  width: 90%;
  height: 30px;
  background: #5b6270;
  border-radius: 3px;
  margin: 15px auto;
}

.menu-icon {
  transition: all 0.3s;
}

.rotate-icon {
  transform: rotate(-90deg);
}

.menu-item span {
  display: inline-block;
  overflow: hidden;
  width: 69px;
  text-overflow: ellipsis;
  white-space: nowrap;
  vertical-align: bottom;
  transition: width 0.2s ease 0.2s;
}

.menu-item i {
  transform: translateX(0px);
  transition: font-size 0.2s ease, transform 0.2s ease;
  vertical-align: middle;
  font-size: 16px;
}

.collapsed-menu span {
  width: 0px;
  transition: width 0.2s ease;
}

.collapsed-menu i {
  transform: translateX(5px);
  transition: font-size 0.2s ease 0.2s, transform 0.2s ease 0.2s;
  vertical-align: middle;
  font-size: 22px;
}

.span-controle {
  /* //绀蓝#494e8f */
  color: #494e8f;
  font-size: 20px;
}

.textarea-screen {
  margin: 10px;
  width: 80%;
  height: 100%;
  background: #d7dde4;
  color: #5b6270;
  border: 0;
  border-radius: 10px;
  padding: 10px;
  
}

.row-operation {
  display: flex;
  justify-content: center;
  border-radius: 5px;
  background: #d9d6c3;
  margin: 1px;
}

.div-com {
  display: flex;
  justify-content: center;
  border-radius: 5px;
  /* background: #d3d7d4; */
  padding: 5px;
  height: 50px;
  margin: 20px;
  color: blue;
}

.div-image {
  display: flex;
  flex-direction: column;
  justify-content: center;
  border-radius: 5px;
  background: #d3d7d4;
  padding: 5px;
}

.img-operation {
  cursor: pointer;
  width: 50px;
  height: 50px;
}

.textarea-python {
  margin-top: 10px;
  width: 100%;
  height: 100%;


}

.div-scroll-back {
  background: white;
  height: 100%;
  padding: 5px;
}

.div-left-control {
  background: white;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  padding: 10px;

}

.div-console {
  background: white;
  height: 45%;
  width: 100%;
  padding: 10px;
  border: 0;
}

.div-work-mode {
  background: white;
  height: 45%;
  width: 100%;
}

.div-row-info {
  height: 40px;
  background: #d3d7d4;
  display: flex;
  align-items: center;
}

.row {
  margin: 1px
}

.div-left-item {
  height: 82px;
  background: #d9d6c3;
  display: flex;
  align-items: center;
}

.div-right-item {
  height: 82px;
  background: #d9d6c3;
  display: flex;
  align-items: center;
}

.div-select-com {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border-radius: 5px;
  padding: 5px;
}

.lab-current-angular {
  width: 100px;
  height: 50px;
  background-color: #2a82e4;
  color: white;
  display: flex;
  vertical-align: middle;
  align-items: center;
  align-content: center;
  justify-content: right;
  padding-right: 15px;
  font-size: 18px;
}

.lab-current-angular-value {
  width: 100px;
  height: 50px;
  background-color: white;
  display: flex;
  vertical-align: middle;
  align-items: center;
  align-content: center;
  justify-content: left;
  padding-left: 15px;
  color: #2a82e4;
  font-size: 18px;
}

.config-button {
  width: 100px;
  height: 50px;
  background-color: #2a82e4;
  color: white;
  display: flex;
  vertical-align: middle;
  align-items: center;
  align-content: center;
  justify-content: center;
  font-size: 18px;
  margin: 15px;
}

.radio-modal-setting {
  display: flex;
}

.radio-items {
  display: flex;
  vertical-align: middle;
  align-items: center;
  align-content: center;
  justify-content: center;
}

.div-radio-params {
  width: 100%;
  display: flex;
  vertical-align: middle;
  justify-content: space-between;
  /* margin: 10px; */
  background-color: #d3d7d4;

  /* padding: 10px; */
}

.label-title {
  display: flex;
  vertical-align: middle;
  align-items: center;
  align-content: center;
  justify-content: center;
  margin: 5px;
  width: 75px;
}
.input-params{  
  margin-top: 10px;
  margin-bottom: 10px;
  width: 150px;
}
.button-params{  
  margin: 5px;
}
.bottom-row{
  padding: 15px;
  bottom: 5px;
  display: flex;
  vertical-align: middle;
  align-items: center;
  align-content: center;
  justify-content: center;

}
.row-middle{
  height: calc(100% - 150px);
}

</style>

<template>
  <div class="layout">
    <Row>
      <i-col span=8>
        <Row class="row-operation">
          <div class="div-left-item">
            <label class="lab-current-angular">
              <span>当前角度</span></label>
            <label class="lab-current-angular-value">{{ formatAngular(currentAngularValue) }}</label>
          </div>
        </Row>
      </i-col>
      <i-col span=16>
        <Row class="row-operation">
          <div class="div-right-item">
            <label class="config-button" @click="onClickProtocolConfig">传输协议</label>
            <label class="config-button" @click="onClickSensorManagement">传感器</label>
            <label class="config-button" @click="onClickConfigSerial">串口</label>
          </div>

        </Row>
      </i-col>
    </Row>
    <Row class="row-middle" id="row-middle">
      <i-col span=8>
        <div class="div-left-control">

          <div class="div-work-mode">
            <RadioGroup v-model="runMode" vertical style="width: 300px;">
              <Radio label="settingMode">
                <Icon></Icon>
                <span>设定模式</span>
              </Radio>
              <div class="div-radio-params">
                <label class="label-title">角度(°)</label>
                <!-- :formatter="value => `${formatAngular(value)}`" -->
                <Input class="input-params"  v-model="angularGoTo" :number=true  type="number"  >
                  <template #content>
                    <div>{{ formatNumber }}</div>
                  </template>
                </Input>

                <!-- <InputNumber class="input-params" :max="180.000" :min="-180.000" v-model="angularGoTo" :step="0.001"  
                  :parser="value => value.replace('°', '')" /> -->
                <Button type="primary" style="visibility:hidden;margin:10px" >启动</Button>
                <Button type="primary" :disabled="runMode=='stepMode'"  style="margin:10px;"  @click="gotoAngular(0)">启动</Button>
              </div>
              <Radio label="stepMode">
                <Icon></Icon>
                <span>步进模式</span>

              </Radio>

              <div class="div-radio-params">
                <label class="label-title">步幅(°)</label>
                <!-- :formatter="value => `${formatAngular(value)}`" -->
                <Input class="input-params" v-model="angularGoStep" :number=true type="number" >
                  <template #content>
                    <div>{{ formatNumber }}</div>
                  </template>
                </Input>
                <!-- <InputNumber  class="input-params" :max="180.000" :min="-180.000" v-model="angularGoStep" :step="0.001" 
                  :parser="value => value.replace('°', '')" /> -->
                <Button type="primary"  :disabled="runMode=='settingMode' || boolStepmotorMoving"  style="margin:10px;"  @click="gotoAngular(1)">增加</Button>
                <Button   :disabled="runMode=='settingMode' || boolStepmotorMoving"  style="margin:10px;"  type="primary" @click="gotoAngular(-1)">减少</Button>
              </div>
            </RadioGroup>
          </div>
          
          <div><Button type="warning" style="width:300px" @click="stopMotor">停止</Button></div>
          <!-- <div class="div-console">
            <textarea ref="main_console" id="main_console" class="textarea-screen" v-model="pythonMessage">
              </textarea>
          </div> -->
        </div>
      </i-col>
      <i-col span=16>
        <div class="div-scroll-back">
          <Scroll ref="left_scroll" :height="divScrollHeight">
            <Table width="100%" :height="divScrollHeight-20" border :columns="scalColumns" :data="scalData"></Table>
          </Scroll>
        </div>
      </i-col>
    </Row>
    <Row class="bottom-row">      
      <i-col id="pywebview-status" span="4">正在准备数据</i-col>
      <i-col span="4">编码器端口: {{comAngularEncoder}}</i-col>
      <i-col span="4">步进电机端口: {{comStepMotor}}</i-col>
      <i-col span="4">传输协议: {{protocol}}</i-col>
      <i-col span="4">※标定数据※</i-col>
      <i-col span="4"><Button type="primary" :disabled="sensorDetectEnabled" @click="onClickStartCollection">启动</Button>
        <Button type="primary" :disabled="!sensorDetectEnabled" @click="onClickStopCollection">停止</Button>
        <Button type="primary" @click="onClickInsertCalibrationRow">保存数据</Button></i-col>
    </Row>
    <serial-config ref="serialConfig" 
    v-if="showSerialConfig"  
    :visible="showSerialConfig" 
    :modalShow="showSerialConfig" 
    @onClickOk="onClickConfigOK"></serial-config>

    
    <protocol-config ref="protocolConfig" 
    v-if="showProtocolConfig"  
    :visible="showProtocolConfig" 
    :modalShow="showProtocolConfig" 
    @onClickOk="onClickProtocolConfigOK"></protocol-config>

    <sensor-management ref="sensorManagement" 
    v-if="showSensorManagement"  
    :visible="showSensorManagement" 
    :modalShow="showSensorManagement" 
    @onClickOk="onClickSensorManagementOK" ></sensor-management>
    
    <!-- <Modal v-model="showSensorManagement" title="传感器管理" width="1080" @on-ok="ok" @on-cancel="cancel">
        <div class="div-modal-content">
            <Card :bordered="false">
                <template #title>
                    <Row>
                        <i-Col span="4" class="col_caption"><span>传感器表</span></i-Col>
                        <i-Col span="8" class="col_caption"><span></span></i-Col>
                        <i-Col span="12" class="col_caption">
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

    </Modal> -->

  </div>
</template>

<script>
import SerialConfig from './modules/serialsConfig.vue'
import SensorManagement from './modules/sensorManagement.vue'
import ProtocolConfig from './modules/protocolConfig.vue'

import ExcelUtils from "@/js/excel.js"
import protocolConfigVue from './modules/protocolConfig.vue'

function pyError(params, callback) {

  let strParam = JSON.stringify(params)
  pywebview.api.on_error(strParam).then(res => {
    // alert(res)
    let jsonRsult = JSON.parse(res)
    callback(jsonRsult)
  })
}

function pyGetSerialList(params, callback) {
  let strParam = JSON.stringify(params)
  pywebview.api.getSerialList().then(res => {
    // alert(res)
    // let jsonRsult = JSON.parse(res)
    callback(res)
  })
}

function pyGetConfigInfo(that){
  pywebview.api.getOption("ANGULAR_ENCODER", "port").then(res => {          
    that.comAngularEncoder = res
  })
  pywebview.api.getOption("STEP_MOTOR", "port").then(res => {      
    that.comStepMotor = res
  })
  
  pywebview.api.getOption("SENSOR_PARAMS", "protocol").then(res => {      
    that.protocol = res
  })
}

function pyGetSensorList(callback){
  pywebview.api.getSensorList().then(res => {          
    callback(res)
  })
}

function pyInsertCalibrationRow(rows, callback){
  pywebview.api.insertCalibrationRow(rows).then(res => {          
    callback(res)
  })
}
function pyGotoAngular(params, callback){
  let strParams = JSON.stringify(params)
  pywebview.api.gotoAngular(strParams).then(res => {          
    callback(res)
  })
}

function pyStopMotor(params, callback){
  let strParams = JSON.stringify(params)
  pywebview.api.stopMotor(strParams).then(res => {          
    callback(res)
  })
}

function pyStartCollection(params, callback){
  // let strParams = JSON.stringify(params)
  pywebview.api.startCollection().then(res => {          
    callback(res)
  })
}

function pyStopCollection(params, callback){
  // let strParams = JSON.stringify(params)
  pywebview.api.stopCollection().then(res => {          
    callback(res)
  })
}

export default {
  components: {
    SerialConfig,
    SensorManagement,
    ProtocolConfig
  },
  data() {
    return {
      divScrollHeight: 900,
      runMode: "settingMode",
      excelSensorList: "",
      comAngularEncoder: "",
      comStepMotor: "",
      showSerialConfig: false,
      showSensorManagement: false,
      showProtocolConfig: false,
      showSensor: false,
      angularGoTo: 5.0,
      angularGoStep: 1.0,
      vertical: 'apple',
      value: "",
      currentAngularValue: 0,
      checkAllChannels: false,
      pythonMessage: "python message",
      comInstrumentName: "",
      protocol: "",
      sensorDetectEnabled: false,
      boolStepmotorMoving: false,
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
      scalColumns: [
        // {
        //   type: 'selection',
        //   width: 60,
        //   align: 'center',
        //   fixed: "left",
        // },
        {
          title: "序号",
          key: "id",
          width: 75
        },
        {
          title: "传感器编号",
          key: "sensorCode",
          width: 150,
        },
        {
          title: "端口",
          key: "sensorCom",
          width: 100,
        },
        {
          title: "地址",
          key: "sensorAddr",
          width: 75,
        },

        {
          title: "类型",
          key: "sensorType",
          width: 75,
        },

        {
          title: "通道",
          key: "channel",
          width: 75,
        },

        {
          title: "测量值",
          key: "sensorValue",
          width: 100,
        },
        {
          title: "AD值",
          key: "adValue",
          width: 150,
        },
        {
          title: "状态",
          key: "status",
          width: 150,
        }
      ],
      scalData: [
        {
          id: "1",
          sensorCode: "92001001",
          sensorCom: "COM10",
          sensorAddr: "1",
          sensorType: "31",
          channel: 1,
          sensorValue: 0.0000,
          adValue: "0000FFFF",
          calibrateDate:"",
          status: "",
          stability : 0
        },
        {
          id: "2",
          sensorCode: "92001001",
          sensorCom: "COM10",
          sensorAddr: "3",
          sensorType: "30",
          channel: 1,
          sensorValue: 0.0000,
          adValue:"0000FFFF",
          calibrateDate:"",
          status: "",
          stability : 0
        },
        {
          id: "3",
          sensorCode: "92001001",
          sensorCom: "COM10",
          sensorAddr: "3",
          sensorType: "32",
          channel: 1,
          sensorValue: 0.0000,
          adValue: "0000FFFF",
          calibrateDate:"",
          status: "",
          stability : 0
        },
      ],
      
    }
  },
  computed: {
      formatNumber () {
          if (this.value === '') return 'Enter number';
          function parseNumber(val) {
            let sign = val< 0?'-':''
            val = Math.abs(val)
            let valInt = Math.trunc(val)
            let demical = Math.trunc((val * 10000))%10000
            if(Math.trunc((val * 10000))%10000 >=1000 ){
              // .1, 5.1000
              return sign + valInt + '.' + demical
            }
            else if(Math.trunc((val * 10000))%10000 >=100 ){
              // .010, 5.0100
              return sign + valInt + '.'  + '0'+ demical + '°'
            }     
            else if(Math.trunc((val * 10000))%10000 >=10 ){
              // .010, 5.0010
              return sign + valInt + '.'  + '00'+ demical + '°'
            }     
            else if(Math.trunc((val * 10000))%10000 >=1 ){
              // .001 ,5.001, 1.0001
              return sign + valInt + '.000' + demical +  '°'
            }    
            else if(Math.trunc((val * 10000))%10000 >=0 ){
              // .,5
              return sign + valInt + '.' + '0000°'
            }
          }
          return parseNumber(this.value);
      },
  },
  created() {
  },
  mounted() {
    this.$Message.config({
        top: 300,
        duration: 5
    });
    let local = this;
    /* let val = this.$root.windowState.winHeight */
    window.addEventListener('pywebviewready', function() {
        var container = document.getElementById('pywebview-status')
        container.innerHTML = '配置信息'

        pywebview.api.getOption("ANGULAR_ENCODER", "port").then(res => {
          console.log( res )
          local.comAngularEncoder = res
        })
        pywebview.api.getOption("STEP_MOTOR", "port").then(res => {
          console.log( res )
          local.comStepMotor = res
        })
        
        pywebview.api.getOption("SENSOR_PARAMS", "protocol").then(res => {
          console.log( res )
          local.protocol = res
        })
        local.loadSensorList()
    })

    window.addEventListener('pythonEvent', function (e) {
      console.log(e)
      /* local.$Message.info( e.data.msg ); */
      local.pythonMessage += "\r\n" + e.data.msg + "\r\n" + e.data.value
      local.parseEvnet(e)

    }, true);
    
    window.addEventListener('pyLiveData', function (e) {
      // console.log(e)
      /* local.$Message.info( e.data.msg ); */
      // local.pythonMessage += "\r\n" + e.data.msg + "\r\n" + e.data.value
      local.parseLiveData(e)

    }, true);

    let divScroll = document.getElementById("row-middle")
    this.divScrollHeight = divScroll.offsetHeight -10
    
  },
  activated(){    
    let that = this
    pyGetSerialList({}, res=>{
      console.log( res )
      that.serialList = res.listmodal
    })
  },
  methods: {
    parseEvnet(evt) {
      if (evt.data.msg == "currentAngularValue") {
        this.currentAngularValue = evt.data.value
      }      
      else if (evt.data.msg == "COLLECT_SENSOR_VALUE") {
          // {ID:0, VALUE:75.31871032714844}
          let jsonValue = JSON.parse(evt.data.value)
          this.scalData.filter(e=>{
            if (e.id ==jsonValue.ID ){
              e.calibrateDate = jsonValue.calibrateDate
              let updatedValue = this.formatAngular(jsonValue.VALUE.toFixed(5))
              if(e.sensorValue != updatedValue ){
                e.stability = 0
              }
              else{
                e.stability = e.stability + 1
              }
              e.sensorValue = this.formatAngular(jsonValue.VALUE.toFixed(5))
              if( e.stability >= 3){
                e.status = "OK 已稳定"
              }
              else{
                e.status = "OK-" + e.stability
              }
            }
          })
      }
      else if (evt.data.msg == "COLLECT_AD_VALUE") {
          // {ID:0, VALUE:75.31871032714844}
          let jsonValue = JSON.parse(evt.data.value)
          this.scalData.filter(e=>{
            if (e.id ==jsonValue.ID ){
              e.calibrateDate = jsonValue.calibrateDate
              e.adValue = jsonValue.VALUE
              e.status = "OK"
            }
          })
      }
      else if (evt.data.msg == "STEPMOTOR_STOP") {
        this.boolStepmotorMoving = false
        this.$Message.info("平台到达设定角度")
      }
    },
    parseLiveData(evt) {
      if (evt.data.msg == "currentAngularValue") {
        this.currentAngularValue = evt.data.value
      }
    },
    setParams() {
      pyError("hello")
    },
    stopMotor(){
      let that = this
      pyStopMotor({},res =>{
        console.log(res)
          if(res.code == 200){
            that.pythonMessage += "\r\nmessage" + res.message
          }
      })
      this.boolStepmotorMoving = false
    },
    gotoAngular( mode ){
      let that = this
      this.boolStepmotorMoving = true
      if( mode == 0){
        let params ={
          targetAngular: Number(this.angularGoTo).toFixed(3)
        }
        pyGotoAngular(params, res=>{
          console.log(res)
          if(res.code == 200){
            that.pythonMessage += "\r\nmessage" + res.message
            that.$Message.info("电机已启动")
          }
          else{
            that.$Message.error("电机启动失败")
          }
        })
      }
      else if( mode == 1 ){
        let params ={
          targetAngular: Math.trunc(Number(this.currentAngularValue)*1000)/1000 + Number(this.angularGoStep)
        }
        pyGotoAngular(params, res=>{
          console.log(res)
          if(res.code == 200){
            that.pythonMessage += "\r\nmessage" + res.message
            that.$Message.info("电机已启动")
          }
          else{
            that.$Message.error("电机启动失败")
          }
        })
      }
      
      else if( mode == -1 ){
        let params ={
          targetAngular: Math.trunc(Number(this.currentAngularValue)*1000)/1000 - Number(this.angularGoStep)
        }
        pyGotoAngular(params, res=>{
          console.log(res)
          if(res.code == 200){
            that.pythonMessage += "\r\n" + "电机启动"
            that.$Message.info("电机已启动")
          }
          else{
            that.$Message.error("电机启动失败")
          }
        })
      }
    },
    onClickProtocolConfig(){
      this.showProtocolConfig = true
      if( this.$refs.protocolConfig ){
        this.$refs.protocolConfig.modal = true
      }
    },    
    onClickConfigSerial(){
      this.showSerialConfig = true
      let that = this
      pyGetSerialList({}, res=>{
        console.log( res )
        that.serialList = res.list
        if( this.$refs.serialConfig ){
          this.$refs.serialConfig.init(that.serialList)
        }
      })

      if( this.$refs.serialConfig ){
        this.$refs.serialConfig.modal = true
      }
    },    
    onClickSensorManagement(){
      this.showSensorManagement = true
      this.showSensor = true
      if( this.$refs.sensorManagement ){
        this.$refs.sensorManagement.modal = true
      }
    },   
    onClickConfigOK(){
      let that = this
      pyGetConfigInfo(that)
    },
    onClickProtocolConfigOK(){
      let that = this
      pyGetConfigInfo(that)
    },
    onClickInsertCalibrationRow(){
      let rows = []
      this.scalData.filter( e=>{
          let row=[]
          row.push(e.id)                
          row.push(e.sensorCode)         
          row.push(e.sensorCom)        
          row.push(e.sensorAddr)          
          row.push(e.sensorType)  
          row.push(e.channel)
          row.push(e.calibrateDate)
          row.push(e.sensorValue.replace("°",""))
          row.push(e.adValue.replace("°",""))
          row.push(this.currentAngularValue)
          rows.push(row)
      })
      let strRows = JSON.stringify(rows)
      pyInsertCalibrationRow(strRows, res=>{
          console.log(res)
          if(res.code == 200){
            this.$Message.info('数据保存成功');
          }
          else{
            this.$Message.error('数据保存失败');
            
          }
      })      
    },
    onClickConfigCancel(){  
    },
    onClickSensorManagementOK(){      
      
    },
    onClickSensorManagementCancel(){
    },
    onClickStartCollection(){
      let that = this
      pyStartCollection({},res =>{
        console.log(res)
          if(res.code == 200){
            that.sensorDetectEnabled = true
            that.pythonMessage += "\r\nmessage" + res.message
            that.scalData.filter(e=>{
              e.status = "STARTED"
            })
          }
      })
    },
    onClickStopCollection(){
      let that = this
      pyStopCollection({},res =>{
        console.log(res)
          if(res.code == 200){
            that.sensorDetectEnabled = false
            that.pythonMessage += "\r\nmessage" + res.message
            that.scalData.filter(e=>{
              e.status = "STOP"
            })
          }
      })
    },
    loadSensorList(){
      let that = this
      pyGetSensorList(res=>{
        that.scalData=[]
        if( res.code == 200 ){
          for( let i in res.result){
            let item ={
              id: res.result[i][0],
              sensorCode: res.result[i][1],
              sensorCom: res.result[i][2],
              sensorAddr: res.result[i][3],
              sensorType: res.result[i][4],
              channel: res.result[i][5],
              sensorValue: that.formatAngular(0.0000),
              status: ""
            }
            that.scalData.push(item)
          }
        }
      })
    },
    formatAngular(val){
      let sign = val< 0?'-':''
      val = Math.abs(val)
      let valInt = Math.trunc(val)
      let demical = Math.trunc((val * 10000))%10000
      if(Math.trunc((val * 10000))%10000 >=1000 ){
        // .1, 5.1000
        return sign + valInt + '.' + demical + '°'
      }
      else if(Math.trunc((val * 10000))%10000 >=100 ){
        // .010, 5.0100
        return sign + valInt + '.'  + '0'+ demical + '°'
      }     
      else if(Math.trunc((val * 10000))%10000 >=10 ){
        // .010, 5.0010
        return sign + valInt + '.'  + '00'+ demical + '°'
      }     
      else if(Math.trunc((val * 10000))%10000 >=1 ){
        // .001 ,5.001, 1.0001
        return sign + valInt + '.000' + demical +  '°'
      }    
      else if(Math.trunc((val * 10000))%10000 >=0 ){
        // .,5
        return sign + valInt + '.' + '0000°'
      }
      else{
        return sign + valInt + '°'
      }
      // 5.001
    }
    // end of methods

  },
}
</script>