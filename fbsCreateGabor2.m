function fb = fbsCreateGabor(rot, RF_siz, Div)
% adapted by David A. Mely from: function init_gabor(rot, RF_siz, Div)
% Thomas R. Serre
% Feb. 2003

% Parameters inherited from original Thomas R. Serre MATLAB implementation
% Those parameters were not modified apart from rot (number of orientations); these are
% biologically constrained from V1 physiology (cf. Serre's thesis work at MIT)
%--------------------------------------------------------------------------------------------------
numFilterSizes      = length(RF_siz);
numSimpleFilters    = numel(rot);
lambda              = RF_siz*2./Div;
sigma               = lambda.*0.8;
G                   = 0.3;   % spatial aspect ratio: 0.23 < gamma < 0.92

% Added: support for full quadrature
%--------------------------------------------------------------------------------------------------
phases              = [0 pi/2];


% Filter in cell array format
%--------------------------------------------------------------------------------------------------
fb                  = cell(2*numSimpleFilters, numFilterSizes);

for k = 1:numFilterSizes  
    for r = 1:numSimpleFilters
        
        % Parameters
        %-----------
        theta     = rot(r)*pi/180;
        filtSize  = RF_siz(k);
        center    = ceil(filtSize/2);
        filtSizeL = center-1;
        filtSizeR = filtSize-filtSizeL-1;
        sigmaq    = sigma(k)^2;
        
        
 
        
        % Compute filter values
        %----------------------
        for iPhi = 1:2
            for i = -filtSizeL:filtSizeR
                for j = -filtSizeL:filtSizeR
                    
                    if ( sqrt(i^2+j^2)>filtSize/2 )
                        E                   = 0;
                    else
                        x                   = i*cos(theta) - j*sin(theta);
                      
                        y                   = i*sin(theta) + j*cos(theta);
                        
                        E                   = exp(-(x^2+G^2*y^2)/(2*sigmaq))*cos(2*pi*x/lambda(k) + phases(iPhi));
                        
                    end
                   
                    
                    f(j+center,i+center)    = E;
                    
                end
            end
            
            % Normalize filter
            %-----------------
            f                               = f - mean(mean(f));
            f                               = f ./ sqrt(sum(sum(f.^2))); 
%           
            disp(2*r - iPhi + 1)
            disp(k)
            fb{2*r - iPhi + 1, k}           = f;
            

        end
    end
end



end