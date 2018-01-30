function [ROI] = read_ImageJ_roi(roi_file, r, c)

% read_imageJ_roi - FUNCTION Read an ImageJ ROI
%

% Author: Ke Zhao <kezhaomy@gmail.com>
% Created: 2017.10.16

% 20180104 Add Oval roi type
% 20180106 Add type support: Freehand, Oval, Rectangle, Polygon
% 20180116 Remove dicom reading part

%% Reading roi
[sROI] = ReadImageJROI(roi_file) ;

switch sROI.strType
    case {'Polygon', 'Freehand'}
        ROI_xy = sROI.mnCoordinates ;
    case 'Rectangle'
        TLBR = sROI.vnRectBounds ; % TOP; LEFT; BOTTOM; RIGHT
        x = [TLBR(1):TLBR(3) TLBR(3):(-1):TLBR(1)]' ;
        y = [TLBR(2)*ones((TLBR(3) - TLBR(1) + 1), 1); ...
            TLBR(4)*ones((TLBR(3) - TLBR(1) + 1), 1) ] ;
        ROI_xy = [y x] ;
    case 'Oval'
        roi_rec = sROI.vnRectBounds ;
        roi_center = [(roi_rec(1) + roi_rec(3)) ...
            (roi_rec(2) + roi_rec(4))] / 2 ;
        a = roi_rec(3) - roi_center(1) ;
        b = roi_rec(4) - roi_center(2) ;
        t = 0:0.05:2*pi;
        x = round(roi_center(1) + a*cos(t)) ;
        y = round(roi_center(2) + b*sin(t)) ;
        ROI_xy = [y' x'] ;
    otherwise
        error('ROI type not support.')
end

%% Creating ROI
%r = rc(1) ;
%c = rc(2) ;
ROI = zeros(r, c) ;
ROI = roipoly(ROI, ROI_xy(:,1), ROI_xy(:,2)) ; 
ROI = uint16(ROI) ;

end

%% NOTE

