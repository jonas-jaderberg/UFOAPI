/**
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech) (7.8.0).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
package org.openapitools.api;

import org.openapitools.model.ExchangheInformation;
import io.swagger.v3.oas.annotations.ExternalDocumentation;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.Parameter;
import io.swagger.v3.oas.annotations.Parameters;
import io.swagger.v3.oas.annotations.media.ArraySchema;
import io.swagger.v3.oas.annotations.media.Content;
import io.swagger.v3.oas.annotations.media.Schema;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.security.SecurityRequirement;
import io.swagger.v3.oas.annotations.tags.Tag;
import io.swagger.v3.oas.annotations.enums.ParameterIn;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.context.request.NativeWebRequest;
import org.springframework.web.multipart.MultipartFile;

import javax.validation.Valid;
import javax.validation.constraints.*;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import javax.annotation.Generated;

@Generated(value = "org.openapitools.codegen.languages.SpringCodegen", date = "2024-09-12T12:02:17.317314499Z[Etc/UTC]", comments = "Generator version: 7.8.0")
@Validated
@Tag(name = "developers", description = "Operations available to regular developers")
public interface KeepaliveApi {

    default Optional<NativeWebRequest> getRequest() {
        return Optional.empty();
    }

    /**
     * GET /keepalive : DATEX II snapshot pull
     * Keepalive 
     *
     * @return Result from keepalive (status code 200)
     */
    @Operation(
        operationId = "keepAlive",
        summary = "DATEX II snapshot pull",
        description = "Keepalive ",
        tags = { "developers" },
        responses = {
            @ApiResponse(responseCode = "200", description = "Result from keepalive", content = {
                @Content(mediaType = "application/json", schema = @Schema(implementation = ExchangheInformation.class))
            })
        }
    )
    @RequestMapping(
        method = RequestMethod.GET,
        value = "/keepalive",
        produces = { "application/json" }
    )
    
    default ResponseEntity<ExchangheInformation> keepAlive(
        
    ) {
        getRequest().ifPresent(request -> {
            for (MediaType mediaType: MediaType.parseMediaTypes(request.getHeader("Accept"))) {
                if (mediaType.isCompatibleWith(MediaType.valueOf("application/json"))) {
                    String exampleString = "{ \"messageType\" : { \"extendedValueG\" : \"extendedValueG\", \"value\" : \"CISFeedback\" }, \"exchangeInformationExtensionG\" : { \"key\" : \"\" }, \"dynamicInformation\" : { \"completedPaylod\" : true, \"returnInformation\" : { \"returnStatus\" : { \"extendedValueG\" : \"extendedValueG\", \"value\" : \"ack\" }, \"returnInformationExtensionG\" : { \"key\" : \"\" }, \"returnStatusReason\" : { \"values\" : [ { \"lang\" : \"lang\", \"value\" : \"value\" }, { \"lang\" : \"lang\", \"value\" : \"value\" } ] }, \"codedInvalidityReason\" : [ { \"extendedValueG\" : \"extendedValueG\", \"value\" : \"invalidCISInformation\" }, { \"extendedValueG\" : \"extendedValueG\", \"value\" : \"invalidCISInformation\" } ] }, \"exchangeStatusDescription\" : { \"values\" : [ { \"lang\" : \"lang\", \"value\" : \"value\" }, { \"lang\" : \"lang\", \"value\" : \"value\" } ] }, \"dynamicInformationExtensionG\" : { \"key\" : \"\" }, \"exchangeStatus\" : { \"extendedValueG\" : \"extendedValueG\", \"value\" : \"closingSession\" }, \"messageSequencingNumber\" : 0, \"sessionInformation\" : { \"startSession\" : \"2000-01-23T04:56:07.000+00:00\", \"sessionID\" : \"sessionID\", \"sessionInformationExtensionG\" : { \"key\" : \"\" } }, \"messageGenerationTimestamp\" : \"2000-01-23T04:56:07.000+00:00\" }, \"exchangeContext\" : { \"supplierOrCisRequester\" : { \"internationalIdentifier\" : { \"country\" : \"country\", \"nationalIdentifier\" : \"nationalIdentifier\", \"internationalIdentifierExtensionG\" : { \"key\" : \"\" } }, \"agentExtensionG\" : { \"key\" : \"\" }, \"address\" : \"address\", \"name\" : \"name\", \"serviceURL\" : \"serviceURL\", \"referenceID\" : \"referenceID\" }, \"operatingMode\" : { \"extendedValueG\" : \"extendedValueG\", \"value\" : \"conditionTriggered\" }, \"exchangeContextExtensionG\" : { \"key\" : \"\" }, \"exchangeSpecificationVersion\" : \"exchangeSpecificationVersion\", \"codedExchangeProtocol\" : { \"extendedValueG\" : \"extendedValueG\", \"value\" : \"deltaPull\" }, \"nonCodedExchangeProtocol\" : \"nonCodedExchangeProtocol\", \"subscription\" : { \"subscriptionEnd\" : \"2000-01-23T04:56:07.000+00:00\", \"deliveyFrequency\" : 0, \"name\" : \"name\", \"subscriptionStart\" : \"2000-01-23T04:56:07.000+00:00\", \"validity\" : { \"validityTimeSpecification\" : { \"overallEndTime\" : \"2000-01-23T04:56:07.000+00:00\", \"overallPeriodExtensionG\" : { \"key\" : \"\" }, \"overallStartTime\" : \"2000-01-23T04:56:07.000+00:00\" }, \"validityExtensionG\" : { \"key\" : \"\" }, \"validityStatus\" : { \"extendedValueG\" : \"extendedValueG\", \"value\" : \"active\" } }, \"referenceID\" : { \"idG\" : \"idG\" }, \"subscriptionExtensionG\" : { \"key\" : \"\" } }, \"updateMethod\" : { \"extendedValueG\" : \"extendedValueG\", \"value\" : \"allElementUpdate\" }, \"clientOrCisProvider\" : [ { \"internationalIdentifier\" : { \"country\" : \"country\", \"nationalIdentifier\" : \"nationalIdentifier\", \"internationalIdentifierExtensionG\" : { \"key\" : \"\" } }, \"agentExtensionG\" : { \"key\" : \"\" }, \"address\" : \"address\", \"name\" : \"name\", \"serviceURL\" : \"serviceURL\", \"referenceID\" : \"referenceID\" }, { \"internationalIdentifier\" : { \"country\" : \"country\", \"nationalIdentifier\" : \"nationalIdentifier\", \"internationalIdentifierExtensionG\" : { \"key\" : \"\" } }, \"agentExtensionG\" : { \"key\" : \"\" }, \"address\" : \"address\", \"name\" : \"name\", \"serviceURL\" : \"serviceURL\", \"referenceID\" : \"referenceID\" } ] } }";
                    ApiUtil.setExampleResponse(request, "application/json", exampleString);
                    break;
                }
            }
        });
        return new ResponseEntity<>(HttpStatus.NOT_IMPLEMENTED);

    }

}
