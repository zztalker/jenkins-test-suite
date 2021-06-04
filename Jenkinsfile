pipeline {
    agent { label 'python3' }
    parameters {
        string(
            name: 'PKG_NAME',
            defaultValue: 'empty',
            description: 'Name of package/platform'
        )
        string(
            name: 'GROUP',
            defaultValue: '',
            description: 'parameter for pytest-split'
        )
        string(
            name: 'GROUP_COUNT',
            defaultValue: '',
            description: 'parameter for pytest-split'
        )
    } // parameters
    stages {
        stage('Rename build') {
            steps {
                script {
                    currentBuild.displayName = "#${currentBuild.id} ${PKG_NAME} ${GROUP}-${GROUP_COUNT}"
                }
                script {
                    currentBuild.description = "${currentBuild.absoluteUrl}"
                }
            } // steps
        } //stage Rename build
      stage('Print params') {
          steps {
                echo "${params.PKG_NAME}"
                echo "${params.GROUP}"
                echo "${params.GROUP_COUNT}"

          }
      } // stage Print params
      stage('Run test') {
          steps {
              sh 'python3 -m pip install -r requirements.txt'
              sh "python3 -m pytest -v --splits ${params.GROUP_COUNT} --group ${params.GROUP} --junitxml=report.xml ."
          }
      } // stage Run test
   } // stages
   post {
        always {
            echo 'Add information about package/platform to test results'
            sh 'python3 junit_xml_add.py . ${PKG_NAME}'
            echo 'Archive artifacts and tests results'
            archiveArtifacts allowEmptyArchive: true, artifacts: '*.xml', followSymlinks: false
            junit allowEmptyResults: true, testResults: 'report.xml'
            script {
                def build = currentBuild.rawBuild
                def result = build.getAction(hudson.tasks.junit.TestResultAction.class).result

                if (result == null) {
                    println("No test results")
                } else if (result.failCount < 1) {
                    println("No failures")
                } else {
                    println("overall fail count: ${result.failCount}")
                }
                failedTests = result.getFailedTests();
                failedTests.each { test ->
                    test.description = "${PKG_NAME} ${GROUP}-${GROUP_COUNT} ${test.getFullName()}";
                }
                cleanWs notFailBuild: true
            }
        }
    } // post
} // pipeline
