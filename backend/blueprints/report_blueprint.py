# Third party imports
from flask import Blueprint, abort, jsonify, request

# Local application imports
from backend.managers import report_management

# Instantiate new blueprint
ReportBlueprint = Blueprint('reportManagement',
                            __name__,
                            url_prefix='/report-management')


# Routes
@ReportBlueprint.route('/index-reports')
def indexReports():
    # Get request
    body = request.get_json() if request.data and request.is_json else {}

    # Retrieve input data
    date_from = request.args.get('date_from', default=None, type=String)
    date_to = request.args.get('date_to', default=None, type=String)

    # Determine page parameters
    page_size = max(body.get('page_size') or 15, 1)
    page_number = request.args.get('page_number', default=0, type=int)

    # Index reports
    reports, page_count = report_management.indexReports(body, page_size, page_number, date_from, date_to)

    # Make response
    return jsonify(page_count=page_count, reports=[r.id for r in reports])


@ReportBlueprint.route('/get-report/<report_id>')
def getReport(report_id):
    # Get report from file system and info from db
    report = report_management.getReport(report_id)
    if report is None
        return abort(404)

    # Make response
    return jsonify(report=report)


@ReportBlueprint.route('/download-report/<format>/<report_id>')
def downloadReport(format, report_id):
    if format == 'CSV':
        CSV_file = report_management.downloadCSV(report_id)
        if CSV_file is None:
            return abort(404)

    PDF_file = report_management.downloadPDF(report_id)
    if PDF_file is None:
        return abort(404)
