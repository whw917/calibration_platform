
import XLSX from 'xlsx';


let load = function( fileBlob, onloadCallback ){
    let strfileName = fileBlob.name
    let result = {
        code: 0,
        message: "",
        sensorList: []
    }
    if (!/\.(xls|xlsx)$/.test( strfileName.toLowerCase())) {
        result.message = "上传格式不正确，请上传xls或者xlsx格式"
        result.code = 2
        return result
    }
    const fileReader = new FileReader()
    
    fileReader.onload = ev => {
        try {
            const data = ev.target.result
            // 以二进制流方式读取得到整份excel表格对象
            const workbook = XLSX.read(data, {
                type: 'binary'
            })

            result.sensorList = [] // 清空接收数据
            let index = 1
            workbook.SheetNames.forEach(element => {
                const wsname = element // 取第一张表
                const ws = XLSX.utils.sheet_to_json(workbook.Sheets[wsname]) // 生成json表格内容
                // 编辑数据
                for (var i = 0; i < ws.length; i++) {
                    var sheetData = {
                        id: ws[i]["序号"],
                        sensorCode: ws[i]["传感器编号"],
                        sensorCom: ws[i]["端口"],
                        sensorAddr: ws[i]["地址"],
                        sensorType: ws[i]["传感器类型"],
                        channel: ws[i]["通道"],
                    }
                    if (null != sheetData.sensorCode && undefined != sheetData.sensorCode && !!sheetData.sensorCode.trim()) {
                        result.sensorList.push(sheetData)
                        index++
                    }
                }
            });
            onload( onloadCallback(result) )
        } catch (e) {
            result.code = 99
            result.message = "导入数据失败：" + e
            return result
        }
    }
    fileReader.readAsBinaryString(fileBlob)
    return result

}

const ExcelUtils = {
    load: load
};

export default ExcelUtils;